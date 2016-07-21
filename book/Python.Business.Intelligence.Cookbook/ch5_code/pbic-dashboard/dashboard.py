from flask import Flask, send_from_directory, render_template

UPLOAD_FOLDER = '/Users/robertdempsey/Dropbox/Private/Python Business Intelligence Cookbook/Drafts/Chapter 5/ch5_code/pbic-dashboard/charts'
BASE_URL = 'http://127.0.0.1:5000/charts/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def uploaded_file():
    # list the charts to show
    wcd = BASE_URL + 'weather-conditions-distribution.png'
    lcb = BASE_URL + 'light-conditions-boxplot.png'
    lcbwcb = BASE_URL + 'lc-by-wc-boxplot.png'
    cca = BASE_URL + 'casualty-count-all.png'
    cc2 = BASE_URL + 'casualty-count-2000.png'
    cc1980 = BASE_URL + 'casualty-count-1980s.png'

    return render_template('dashboard.html',
                           wcd=wcd,
                           lcb=lcb,
                           lcbwcb=lcbwcb,
                           cca=cca,
                           cc2=cc2,
                           cc1980=cc1980)


@app.route('/charts/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.debug = True
    app.run()
