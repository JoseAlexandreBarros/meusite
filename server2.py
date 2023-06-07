from flask import Flask,render_template, request,flash, redirect
import json

#from flask_sqlalchemy import SQLAlchemy

#db=SQLAlchemy()
#DB_NAME = 'database.db'


app = Flask(__name__)
app.config['SECRET_KEY'] = "segredo"
#app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#db.init_app(app)
logado=False




@app.route("/")
def main_page():
    
    return render_template('meusite2.html',nome_imagem="",nome_imagem2="",nome_imagem3="")

@app.route("/peixe", methods=['POST'])
def peixe():
    if request.method=='POST':
        global pagina_atual
        pagina_atual='peixe'
        return render_template ('/peixe.html')

@app.route("/lula", methods=['POST'])
def lula():
    if request.method=='POST':
        return render_template ('/lula.html')

@app.route("/tub", methods=['POST'])
def tub():
    if request.method=='POST':
        return render_template ('tub.html')

@app.route("/registro", methods=['POST'])
def registro():
    global logado
    if request.method=='POST':
        if request.form['action']=='sair':
            logado=False
            return render_template ('meusite2.html', reg='deslogado')
        if request.form['action'] == 'regi':
            if request.form['nome'] =='' or request.form['senha'] =='':
                return render_template ('meusite2.html', reg='nome ou senha invalida')
            else:
                #a={'usuario':request.form["nome"],'senha': request.form['senha']}
                #b=str(a)
                b=(f"{request.form['nome']},{request.form['senha']}")
                with open("basedados.txt", mode="a") as arquivo:
                    arquivo.write(b +"\n")
                return render_template ('meusite2.html', reg='cadastrado!')
        if request.form['action'] == 'entrar' :
            with open("basedados.txt", mode='r+') as arquivo:
               #while True:
                for line in arquivo:
                    x=line.split(",")
                    user=x[0]
                    user_pass=x[1].strip()
                    if(user == request.form['nome'] and user_pass == request.form['senha'] ):
                        
                        logado=True
                        return render_template ('meusite2.html', reg='logado!')
                return render_template ('meusite2.html', reg='usuario nao cadastrado!')


@app.route("/registro_peixe", methods=['POST'])
def registro_peixe():
    global logado
    if request.method=='POST':
        if request.form['action']=='sair':
            logado=False
            return render_template ('/peixe.html', reg='deslogado')
        if request.form['action'] == 'regi':
            if request.form['nome'] =='' or request.form['senha'] =='':
                return render_template ('/peixe.html', reg='nome ou senha invalida')
            else:
                #a={'usuario':request.form["nome"],'senha': request.form['senha']}
                #b=str(a)
                b=(f"{request.form['nome']},{request.form['senha']}")
                with open("basedados.txt", mode="a") as arquivo:
                    arquivo.write(b +"\n")
                return render_template ('/peixe.html', reg='cadastrado!')
        if request.form['action'] == 'entrar' :
            with open("basedados.txt", mode='r+') as arquivo:
               #while True:
                for line in arquivo:
                    x=line.split(",")
                    user=x[0]
                    user_pass=x[1].strip()
                    if(user == request.form['nome'] and user_pass == request.form['senha'] ):
                        
                        logado=True
                        return render_template ('peixe.html', reg='logado!')
                return render_template ('peixe.html', reg='usuario nao cadastrado!')


@app.route("/registro_lula", methods=['POST'])
def registro_lula():
    global logado
    if request.method=='POST':
        if request.form['action']=='sair':
            logado=False
            return render_template ('/lula.html', reg='deslogado')
        if request.form['action'] == 'regi':
            if request.form['nome'] =='' or request.form['senha'] =='':
                return render_template ('/lula.html', reg='nome ou senha invalida')
            else:
                #a={'usuario':request.form["nome"],'senha': request.form['senha']}
                #b=str(a)
                b=(f"{request.form['nome']},{request.form['senha']}")
                with open("basedados.txt", mode="a") as arquivo:
                    arquivo.write(b +"\n")
                return render_template ('/lula.html', reg='cadastrado!')
        if request.form['action'] == 'entrar' :
            with open("basedados.txt", mode='r+') as arquivo:
               #while True:
                for line in arquivo:
                    x=line.split(",")
                    user=x[0]
                    user_pass=x[1].strip()
                    if(user == request.form['nome'] and user_pass == request.form['senha'] ):
                        
                        logado=True
                        return render_template ('/lula.html', reg='logado!')
                return render_template ('meusite.html', reg='usuario nao cadastrado!')

@app.route("/registro_tub", methods=['POST'])
def registro_tub():
    global logado
    if request.method=='POST':
        if request.form['action']=='sair':
            logado=False
            return render_template ('/tub.html', reg='deslogado')
        if request.form['action'] == 'regi':
            if request.form['nome'] =='' or request.form['senha'] =='':
                return render_template ('tub/.html', reg='nome ou senha invalida')
            else:
                #a={'usuario':request.form["nome"],'senha': request.form['senha']}
                #b=str(a)
                b=(f"{request.form['nome']},{request.form['senha']}")
                with open("basedados.txt", mode="a") as arquivo:
                    arquivo.write(b +"\n")
                return render_template ('tub.html', reg='cadastrado!')
        if request.form['action'] == 'entrar' :
            with open("basedados.txt", mode='r+') as arquivo:
               #while True:
                for line in arquivo:
                    x=line.split(",")
                    user=x[0]
                    user_pass=x[1].strip()
                    if(user == request.form['nome'] and user_pass == request.form['senha'] ):
                        
                        logado=True
                        return render_template ('tub.html', reg='logado!')
                return render_template ('tub.html', reg='usuario nao cadastrado!')

@app.route("/comentario", methods=['POST'])

def comentario():
    if logado==False:
        return render_template('meusite2.html',nao_logado='é necessário logar para comentar') 
    else:
        com_text=request.form['comentario']
        new_text=''
        with open("comentarios.txt", mode='a') as arquivo:
            arquivo.write(com_text +"\n")
        with open("comentarios.txt", mode='r') as arquivo:
            linhas=arquivo.readlines()
           # for linha in linhas:
              #  new_text=(new_text+linha+'\n')
            #com_text=arquivo.read()
        return render_template('meusite2.html',nao_logado=linhas)
        
        
@app.route("/comentario_peixe", methods=['POST'])

def comentario_peixe():
    if logado==False:
        return render_template('/peixe.html',nao_logado_peixe='é necessário logar para comentar') 
    else:
        com_text=request.form['comentario']
        new_text=''
        with open("comentarios.txt", mode='a') as arquivo:
            arquivo.write(com_text +"\n")
        with open("comentarios.txt", mode='r') as arquivo:
            linhas=arquivo.readlines()
            #for linha in linhas:
               # new_text=(new_text+linha+'\n')
            #com_text=arquivo.read()
        return render_template('/peixe.html',nao_logado_peixe=linhas)

@app.route("/comentario_lula", methods=['POST'])

def comentario_lula():
    if logado==False:
        return render_template('/lula.html',nao_logado_lula='é necessário logar para comentar') 
    else:
        com_text=request.form['comentario']
        new_text=''
        with open("comentarios.txt", mode='a') as arquivo:
            arquivo.write(com_text +"\n")
        with open("comentarios.txt", mode='r') as arquivo:
            linhas=arquivo.readlines()
            #for linha in linhas:
                #new_text=(new_text+linha+'\n')
            #com_text=arquivo.read()
        return render_template('/lula.html',nao_logado_lula=linhas)

@app.route("/comentario_tub", methods=['POST'])

def comentario_tub():
    
    if logado==False:
        
        return render_template('/tub.html',nao_logado_tub='é necessário logar para comentar') 
    else:
        com_text=request.form['comentario']
        new_text=''
        with open("comentarios.txt", mode='a') as arquivo:
            arquivo.write(com_text +"\n")
        with open("comentarios.txt", mode='r') as arquivo:
            linhas=arquivo.readlines()
           #for linha in linhas:
               # new_text=(new_text+linha+'\n')
            #com_text=arquivo.read()
        return render_template('/tub.html',nao_logado_tub=linhas)

'''def comentario():
    if logado==False:
        return render_template('meusite.html',nao_logado='é necessário logar para comentar') 
    else:
        com_text=request.form['comentario']
        new_text=''
        with open("comentarios.txt", mode='a') as arquivo:
            arquivo.write(com_text +"\n")
        with open("comentarios.txt", mode='r') as arquivo:
            linhas=arquivo.readlines()
            for linha in linhas:
                new_text=(new_text+linha+'\n')
            #com_text=arquivo.read()
        return render_template('meusite.html',nao_logado=new_text)
        #return 'a'
 '''