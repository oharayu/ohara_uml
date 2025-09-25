from utils import parse_post, render_template
from app_logic import  setFirstValue, setSecondValue
def addnumbers(environ):
    method = environ["REQUEST_METHOD"]

    if method == "POST":
        data = parse_post(environ)
        num1 = data.get("num1", [""])[0]
        num2 = data.get("num2", [""])[0]

        setFirstValue(num1)
        setSecondValue(num2)

        try:
            n1 = int(num1)
            n2 = int(num2)
            result_block = f"<p>{n1} ＋ {n2} ＝ {n1 + n2}</p>"
        except ValueError:
            result_block = "<p style='color:red;'>整数を入力してください</p>"

        return render_template(
            "boundaries/addnumbers_result.html",
            result_block=result_block
        )

    # GET の場合は入力フォームを表示
    return render_template("boundaries/addnumbers_data.html")
