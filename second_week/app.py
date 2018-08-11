from flask import Flask,render_template
import os
import json

app =Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

os.chdir('/home/shiyanlou/files/')

@app.route('/')
def index():
    file_list =os.listdir('/home/shiyanlou/files/')
    title_list = []
    for js in file_list:
        with open(js,'r') as f:
            json_content = json.loads(f.read())
            json_title=json_content['title']
            title_list.append(json_title)
    return render_template('index.html',title_list=title_list)



@app.errorhandler(404)
@app.route('/files/<filename>')
def file(filename):
     
    js = '/home/shiyanlou/files/{}.json'.format(filename)
    if not os.path.exists(js):
        return render_template('404.html'),404
    else:
        with open(js,'r') as f:
            json_content = json.loads(f.read())
            json_con = json_content['content']
        return json_con


#@app.errorhandler(404)
#def not_found(filename):
    #js = '/home/shiyanlou/files/{}.json'.format(filename)
    #if not os.path.exists(js):
        #return render_template('404.html'),404

if __name__=='__main__':
    app.run()
