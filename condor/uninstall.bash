###########################################
# Script para DesInstalacion de Condor    #
#  Edier Alberto Zapata edalzap@gmail.com #
#  Septiembre 2010 Version 0.1/2k100924   #
###########################################
#!/bin/bash

# Detectar Ruta Instalacion Condor
rutaCondor=$(echo $CONDOR_CONFIG | sed 's:/condor_config::'| sed 's:/etc::')

#############################################
###        DECLARACION DE MENSAJES        ###
#############################################
strIdioma="> Seleccione su idioma / Select your language:\n 1. Esp.\n 2. Eng(beta).\nOpcion/Choice";
strRutaBad="> No se Detecto Condor. No existe variable CONDOR_CONFIG";
strRuta="> Detectado Condor en: ";
strProceso="> Deteniendo proceso: ";
strProcesos="> Cancelando procesos condor_*";
strBorrado="> Eliminando Contenido de: ${rutaCondor}";
strBorradoBad="> No posee permisos para eliminar archivos de: ${rutaCondor}";
strInitd="> Removiendo startCondor.sh de init.d";

#############################################
### DECLARACION DE VARIABLES Y CONSTANTES ###

# Opciones que minimizan la edicion del archivo de configuracion.
# UID almacena el ID del usuario que ejecuta el script.
# LOGNAME almacena el login del usuario que ejecuta el script.

#############################################
###    FUNCIONES PARA CAPTURA DE DATOS    ###

# Solicitar idioma deseado para los mensajes
function leeIdioma()
{
 idioma=$1;
 if [ -z $1 ]; then
  echo -n -e "${strIdioma}: "
  read idioma
 fi
# si se elije Ingles, se cambian los mensajes.
 if [ ${idioma} -eq 2 ]; then
  strRuta="> Detected Condor in: ";
  strRutaBad="> Condor not detected. Variable CONDOR_CONFIG not Found.";
  strProceso="> Stoping process: ";
  strProcesos="> Stoping process condor_*";
  strBorrado="> Deleting content in: ${rutaCondor}";
  strBorradoBad="> You can't delete files from: ${rutaCondor}";
  strInitd="> Removing startCondor.sh from init.d";
 fi
}

# Verificar que hay Condor.
function chkCondor()
{
# Verificar que la variable con la ruta de Condor existe.
 if [ -z $CONDOR_CONFIG ]; then
  echo -e "${strRutaBad}"
  exit 1
 fi
 echo -e "${strRuta}\n${rutaCondor}"
}

# Cancelar Procesos de Condor
# No se usa condor_off porque dicho comando solo funciona desde
# el Central Manager. En su lugar se hara un Kill de cada proceso.
function stopCondor()
{
 echo ${strProcesos}
# Listado Procesos Condor en el sistema
 for i in $(ps awux | grep condor_ | grep -v grep | awk '{print $2}');
 do
# mostrar proceso
  proceso=$(ps awux | grep -w $i | grep -v grep)
  echo -e "${strProceso}: ${proceso}";
# matar proceso
  kill -9 $i
 done
}

# Eliminar variables de entorno de la configuración de Bash.
function cambiaBashrc
{
 if [ ${UID} -eq 0 ]; then # Es root se cambia el /etc/bashrc
  if [ -f /etc/bashrc ]; then
   homeBashrc="/etc/bashrc";
  elif [ -f /etc/bash.bashrc ]; then
   homeBashrc="/etc/bash.bashrc";
  fi
# Eliminar configuracion antigua.
  grep -v "TICAC" ${homeBashrc} > /tmp/bashTmp
  cat /tmp/bashTmp > ${homeBashrc}
 else
  homeBashrc="${HOME}/.bashrc";
  homeProfile="${HOME}/.bash_profile";
  echo "${strBash}"
  if [ -f ${homeBashrc} ]; then
# Eliminar configuracion antigua.
    grep -v "TICAC" ${homeBashrc} > /tmp/bashTmp
    cat /tmp/bashTmp > ${homeBashrc}
# Eliminar configuracion antigua.
    grep -v ". ${homeBashrc}" ${homeProfile} > /tmp/bashTmp
    cat /tmp/bashTmp > ${homeProfile}
  else
   echo "if [ -f /etc/bashrc ]; then" > ${homeBashrc}
   echo " . /etc/bashrc         ${strBashEtc}" >> ${homeBashrc}
   echo "fi" >> ${homeBashrc}
# Algunos Bash cargan .bash_profile en lugar de .bashrc
    touch ${homeProfile}
# Eliminar configuracion antigua.
    grep -v ". ${homeBashrc}" ${homeProfile} > /tmp/bashTmp
    cat /tmp/bashTmp > ${homeProfile}
  fi
 fi
}

# Funcion que elimina el script startCondor.sh del inicio
function limpiaInitd
{
 initD=$1
 script=startCondor.sh
 echo "${strInitd}"
# Si no es root no puede acceder a /etc/init.d
 if [ ${UID} -eq 0 ]; then
# Estamos en Debian?
  if [ -f /sbin/update-rc.d -o -f /usr/sbin/update-rc.d ]; then
   update-rc.d -f startCondor.sh remove
   rm -f /etc/init.d/startCondor.sh
# O estamos en RedHat?
  elif [ -f /sbin/chkconfig -o -f /usr/sbin/chkconfig ]; then
# Eliminar del init.d
   chkconfig --del startCondor.sh
   rm -f /etc/init.d/startCondor.sh
  fi
 fi
}

# Funcion encargada de eliminar todos los archivos .dbg
# en ${prefijo}, con el fin de reducir el tamaño en disco.
function borraCondor()
{
 touch ${rutaCondor}/test &> /dev/null
  escribe=$(echo $?)
 if [ ${escribe} -ne 0 ]; then
  echo "${strBorradoBad}"
# Si se usaron argumentos y hay error salir.
# Si no se usaron argumentos seguir preguntando
  if [ -z $1 ]; then
   borraCondor
  else
   exit 1
  fi
 else
  echo "${strBorrado}"
  rm -rf ${rutaCondor}
 fi
}

#############################################
###            CAPTURA DE DATOS           ###
#############################################

# Solicitar Idioma para los mensajes
 if [ -z $1 ]; then
  leeIdioma
 else
  leeIdioma $1
 fi

# Verificar que esta en la carpeta con Condor
 chkCondor

# Iniciar captura opciones instalacion
 stopCondor      # Matar los procesos de Condor en el sistema
 cambiaBashrc    # Quitar variables de entorno de la configuracion de Bash
 limpiaInitd     # Quitar startCondor.sh del inicio del sistema
 borraCondor $1  # Quitar carpeta Condor del sistema

