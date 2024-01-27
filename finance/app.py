import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    """for the user currently logged in, which stocks the user owns, the numbers of shares owned,
    the current price of each stock, and the total value of each holding (i.e., shares times price)"""
    stocks = db.execute("SELECT stock_symbol,shares,price FROM purchase WHERE id_user = ?",session["user_id"])
    user_cash = float(db.execute("SELECT cash FROM users WHERE id = ?",session["user_id"])[0]["cash"])
    total = 0
    for j in stocks:
        total += j["price"]
    return render_template("layout.html",stocks=stocks,cash = usd(user_cash),total=usd(total))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    user_balance = db.execute("SELECT cash FROM users WHERE id = ?",session["user_id"])[0]["cash"]
    username = db.execute("SELECT username FROM users WHERE id = ?",session["user_id"])[0]['username']
    if request.method == "POST":
        stock_quote = lookup(request.form.get("symbol"))
        if not stock_quote:
            return apology("The symbol isn't correct")
        try:
            no_shares = int(request.form.get("shares"))
        except:
            return apology("invalid number")
        if(no_shares <= 0):
            return apology("invalid number")
        total_price = no_shares*stock_quote["price"]
        if(user_balance < total_price):
            return apology("you don't have enough cash")
        db.execute("INSERT INTO purchase(id_user,username,price,stock_symbol,shares,name) VALUES(?,?,?,?,?,?)",session["user_id"],username,total_price,stock_quote["symbol"],no_shares,stock_quote["name"])
        new_balance = user_balance-total_price
        db.execute("UPDATE users SET cash = ?",new_balance)
        return redirect("/")
    else:
        return render_template("buy.html",balance = usd(user_balance),name = username)

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_balance = db.execute("SELECT cash FROM users WHERE id = ?",session["user_id"])[0]["cash"]
    username = db.execute("SELECT username FROM users WHERE id = ?",session["user_id"])[0]['username']
    users_stocks_bought = db.execute("SELECT stock_symbol,name,price,shares FROM purchase WHERE id_user = ?",session["user_id"])
    users_stocks_sold = db.execute("SELECT name,price,shares,symbol FROM sold WHERE id_user = ?",session["user_id"])
    return render_template("history.html",users_stocks_sold=users_stocks_sold,users_stocks_bought=users_stocks_bought)
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/",200)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        stock_quote = lookup(request.form.get("symbol"))
        if not stock_quote:
            return apology("The symbol isn't correct")
        return render_template("quoted.html",stock_name = stock_quote["name"],stock_price = usd(stock_quote["price"]),stock_symbol = stock_quote["symbol"])
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #confirm user typed username
        if not request.form.get("username"):
            return apology("You must type username ")
        elif not request.form.get("password"):
            return apology("You must type password ")
        elif not request.form.get("confirmation"):
            return apology("You must confirm password")
        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("password and confirmation doesn't match")
        elif db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username")):
            return apology("The username is used before try another")
        username = request.form.get("username")
        password = request.form.get("password")
        db.execute("INSERT INTO users(username,hash) VALUES(?,?)",username,generate_password_hash(password))
        session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?",username)[0]["id"]
        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_balance = db.execute("SELECT cash FROM users WHERE id = ?",session["user_id"])[0]["cash"]
    username = db.execute("SELECT username FROM users WHERE id = ?",session["user_id"])[0]['username']
    users_stocks = db.execute("SELECT stock_symbol,shares FROM purchase WHERE id_user = ?",session["user_id"])
    if request.method == "POST":
        stock_quote = lookup(request.form.get("symbol"))
        total_number = 0
        print(users_stocks)
        for i in users_stocks:
            if(i["stock_symbol"] == stock_quote):
                total_number += 1
        try:
            no_shares = int(request.form.get("shares"))
        except:
            return apology("Enter valid number of shares")
        if (not no_shares) or (no_shares <= 0):
            return apology("Enter valid number of shares")
        if no_shares > int(db.execute("SELECT sum(shares) FROM purchase WHERE (id_user = ? AND stock_symbol = ?)",session["user_id"],stock_quote["symbol"])[0]["sum(shares)"]):
            return apology("You don't have That shares of stock")
        total_price = no_shares*stock_quote["price"]
        db.execute("INSERT INTO sold (id_user,username,price,symbol,shares,name) VALUES(?,?,?,?,?,?)",session["user_id"],username,total_price,stock_quote["symbol"],no_shares,stock_quote["name"])
        db.execute("UPDATE users SET cash = ? WHERE id = ?",user_balance + total_price,session["user_id"])
        user_balance = db.execute("SELECT cash FROM users WHERE id = ?",session["user_id"])[0]["cash"]
        initial_shares = db.execute("SELECT sum(shares) FROM purchase WHERE id_user = ? AND stock_symbol = ?",session["user_id"],stock_quote["symbol"])[0]["sum(shares)"]
        if no_shares == initial_shares:
            db.execute("DELETE FROM purchase WHERE (id_user = ? AND stock_symbol = ?)",session["user_id"],stock_quote["symbol"])
        elif no_shares < initial_shares:
            initial_shares -= no_shares
            new_price = initial_shares * stock_quote["price"]
            db.execute("UPDATE purchase SET shares = ?,price = ? WHERE id_user = ? AND stock_symbol = ?",initial_shares,new_price,session["user_id"],stock_quote["symbol"])
        return redirect("/")
    else:
        return render_template("sell.html",user_balance = usd(user_balance),name = username,users_stocks=users_stocks)
