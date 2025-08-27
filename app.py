from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_final_fee(branch, score, course_fee):
    scholarship = 0
    
    
    if branch.lower() == "arts":
        if score >= 90:
            scholarship = 30
        elif score >=75 and score<90: 
            scholarship = 20
        elif score < 75:
            scholarship = 10  
    
    
    elif branch.lower() == "engineering":
        if score >= 90:
            scholarship = 30
        elif score >=75 and score<90:  
            scholarship = 20
        elif score < 75:
            scholarship = 10  
    else:
        return None, None
    
   
    scholarship_amount = course_fee * (scholarship / 100)
    final_fee = course_fee - scholarship_amount
    
    return scholarship, final_fee


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        branch = request.form["branch"]
        score = int(request.form["score"])
        course_fee = float(request.form["course_fee"])

        scholarship, final_fee = calculate_final_fee(branch, score, course_fee)

        if scholarship is None:
            return render_template("result.html", error="Invalid branch entered. Please enter Arts or Engineering.")
        else:
            return render_template(
                "result.html",
                branch=branch.capitalize(),
                score=score,
                course_fee=course_fee,
                scholarship=scholarship,
                final_fee=final_fee
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
