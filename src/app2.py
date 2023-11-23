from flask import Flask,jsonify
from flask_mysqldb import MySQL
from config import config


app=Flask(__name__)

con=MySQL(app)

def leer_alumno_bd(mat):
    try:
        cursor=con.connection.cursor()
        sql="select * from alumnos where matricula={0}".format(mat)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            alumno={'matricula':datos[0],'nombre':datos[1],'apaterno':datos[2],'amaterno':datos[3],'correo':datos[4]}
            return alumno
        else:
            return None
    except Exception as ex:
        raise ex

@app.route('/alumnos',methods=['GET'])
def list_alumnos():
    try:
        cursor=con.connection.cursor()
        sql='select * from alumnos'
        cursor.execute(sql)
        datos=cursor.fetchall()
        listAlumn=[]
        for fila in datos:
            alum={'matricula':fila[0],'nombre':fila[1],'apaterno':fila[2],'amaterno':fila[3],'correo':fila[4]}
            listAlumn.append(alum)

        #print(listAlumn)
        return jsonify({'Alumnos':listAlumn,'mensaje':'Lista de alumnos'})
    
    except Exception as ex:
        return jsonify({'mensaje':'{}'.format(ex)})

@app.route('/alumnos/<mat>',methods=['GET'])
def leer_alumno(mat):
    try:
        alumno=leer_alumno_bd(mat)
        if alumno != None:
            return jsonify({'Alumnos':alumno,'mensaje':'El alumno encontrado','exito':True})
        else:
            return jsonify({'mensaje':'Alumno no encintrado','exito':False})
        
    except Exception as ex:
        return jsonify({'mensaje':'{}'.format(ex),'exito':False})


def pagina_no_encontrada(error):
    return '<h1>Página no encontrada :c</h1>',404

if __name__=="__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()