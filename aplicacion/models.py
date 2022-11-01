from django.db import models


class coordinador(models.Model):
    coor_cedula=models.IntegerField('Cedula', primary_key=True)
    coor_nombre=models.CharField('Nombre', max_length=30)
    coor_apellido=models.CharField('Apellido', max_length=45)
    coor_correo=models.CharField('Correo', max_length=30)
    coor_telefono=models.CharField('Telefono', max_length=10)

    def __str__(self): 
       return "%s %s %s %s %s " % (self.coor_cedula,self.coor_nombre,self.coor_apellido,self.coor_correo,self.coor_telefono)

class docente(models.Model):
    doc_cedula=models.IntegerField('Cedula', primary_key=True)
    doc_nombre=models.CharField('Nombre', max_length=30)
    doc_apellido=models.CharField('Apellido', max_length=45)
    doc_correo=models.CharField('Correo', max_length=30)
    doc_telefono=models.CharField('Telefono', max_length=10)
    
    def __str__(self): 
       return (self.doc_cedula,self.doc_nombre,self.doc_apellido,self.doc_correo,self.doc_telefono)

class horario(models.Model):
    hor_codigo=models.AutoField('Codigo Horario', primary_key=True)
    hor_fechaInicio=models.DateField('Fecha Inicio', null=True)
    hor_fechaFin=models.DateField('Fecha Fin', null=True)
    hor_horaInicio=models.TimeField('Hora Inicio', null=True)
    hor_horaFin=models.TimeField('Hora Fin', null=True)
    coor_cedula=models.ForeignKey(coordinador, on_delete=models.CASCADE)

    def __str__(self): 
       return "%s (%s : %s)" % (self.hor_codigo,self.hor_fechaInicio,self.hor_fechaFin,self.hor_horaInicio('%I:%M %p'),self.hor_horaFin('%I:%M %p'))

class horariodocente(models.Model):
    hordoc_codigo=models.AutoField('Codigo Horario Docente', primary_key=True)
    doc_cedula=models.ForeignKey(docente, on_delete=models.CASCADE, null=True)
    hor_codigo=models.ForeignKey(horario, on_delete=models.CASCADE, null=True)

    def __str__(self): 
       return (self.hordoc_codigo)

class usuario(models.Model):
    user_documento=models.IntegerField('Cedula', primary_key=True)
    user_nombre=models.CharField('Nombre', max_length=30)
    user_apellido=models.CharField('Apellido', max_length=45)
    user_correo=models.CharField('Correo', max_length=30)
    user_usuario=models.CharField('Usuario', max_length=30)
    user_clave=models.CharField('Contraseña', max_length=100)
    user_rol=models.CharField('Rol', max_length=13)
    coor_cedula=models.ForeignKey(coordinador, on_delete=models.CASCADE, null=True)
    
    def __str__(self): 
       return (self.user_documento,self.user_nombre,self.user_apellido,self.user_correo,self.user_usuario,self.user_clave,self.user_rol, self.coor_cedula)