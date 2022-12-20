from flask import Flask
import requests

def current_stats(pos=[[' ', ' ',' '],[' ', ' ',' '],[' ', ' ',' ']]):
    text_box='<input type="text" id="fname" name="fname" size="1"><br><br>'
    ttt_table=f'''
    <div>
    <div>
    Tic-Tac-Toe
    </div>
    <div>
    <form action="http://127.0.0.1:5000">
    <table>
        <tr>
        
        <td>{text_box if pos[0][0]==" " else pos[0][0]}</td>
        <td>{text_box if pos[0][1]==" " else pos[0][1]}</td>
        <td>{text_box if pos[0][2]==" " else pos[0][2]}</td>
        </tr>
        <tr>
        <td>{text_box if pos[1][0]==" " else pos[1][0]}</td>
        <td>{text_box if pos[1][1]==" " else pos[1][1]}</td>
        <td>{text_box if pos[1][2]==" " else pos[1][2]}</td>
        </tr>
        <tr>
        <td>{text_box if pos[2][0]==" " else pos[2][0]}</td>
        <td>{text_box if pos[2][1]==" " else pos[2][1]}</td>
        <td>{text_box if pos[2][2]==" " else pos[2][2]}</td>
        </tr>
    </table>
     <input type="submit" value="Submit">
    </form>
    </div>
    </div>'''
    return ttt_table

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello():
    if Flask.request.method == 'POST':
        print("Hi")
        # return current_stats()
    # initiate_game()
    # usercli
    else:
        return current_stats()



if __name__ == '__main__':
    app.run(debug=True)
