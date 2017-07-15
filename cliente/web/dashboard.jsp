<%-- 
    Document   : dashboard
    Created on : Jun 26, 2017, 12:22:55 PM
    Author     : Jorge
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
           <script src="js/jquery-3.2.1.js"></script>
        <link rel="stylesheet" href="css/bootstrap.min.css">
          <script src="js/bootstrap.min.js"></script>
        <title>JSP Page</title>
    </head>
     <% 
         if (session.getAttribute("usuario") == null)
            {
                response.sendRedirect("/cliente/login.html");
            }
            String strUsuarioActual = (String) session.getAttribute("usuario"); 
            
            out.println(strUsuarioActual);
            
        %>
    <script>
        
        var enjuego = false;
        var x = 0;
        var y = 0;
        var tiempoM = 0;
        var tiempoS = 0;
        var modalidad = 0;
        var disparo = 0;
        var rafagas = 0;
        var usuario = "<% out.print(strUsuarioActual);%>";
        var turno = false;
         var refreshIntervalId = setInterval(juego,1000);
        $(document).ready(function(){
          
        });
        function juego()
        {
           if (enjuego === false)
           {
               revisar();
           }
           else
           {
               if(x == 0 && y ==0)
               {
                   getGame();
               }
               else
               {
                   turnoA();
                   if (turno === true)
                   {
                       $("#turnoDiv").html("Es tu turno");
                       $("#gt").attr("disabled",false);
                       gane();
                   }
                   else
                   {
                       $("#turnoDiv").html("No es tu turno");
                       $("#gt").attr("disabled",true);
                   }
               }
           }
        }
        function listarusuarios()
        {
            $.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,tipo:"listausuarios"},
                    success: function(response) {
                            //console.log(response);
                         var res = response.trim();
                         var res2 = res.split(",");
                         var inset = "";
                         for ( var i =1 ; i < res2.length ; i++)
                         {
                             inset = inset + "<option>"+res2[i]+"</option>"
                         }
                         $("#listausuarios").html(inset);
                        },
                    error: function(error) {
                         console.log(error);
                    }
            });
            
        }
        function eliminarus()
        {
            var us =  $("#listausuarios").val();
            $.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:us,tipo:"eliminarus"},
                    success: function(response) {
                           console.log(response);
                           listarusuarios();
                        },
                    error: function(error) {
                         console.log(error);
                    }
            });
            
             
        }
        function editarus()
        {
            var us =  $("#listausuarios").val();
            var contra = $("#contranueva").val();
            $.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:us,contra:contra,tipo:"editarus"},
                    success: function(response) {
                           console.log(response);
                           
                        },
                    error: function(error) {
                         console.log(error);
                    }
                     });
       }
        function AgregarNave()
        {
            var afila = $("#adfila").val();
            var acol = $("#adcol").val();
            var anave = $("#adnave").val();
            var amodo = $("#modo").val();
            data = {usuario:usuario,fila:afila,tipo:"insert",col:acol,nave:anave,modo:amodo,dire:adirec};
            var adirec = $("#direct").val();
             	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,fila:afila,tipo:"insert",col:acol,nave:anave,modo:amodo,dire:adirec},
                    success: function(response) {
                            //console.log(response);
                         rellenar(1);
                            rellenar(2);
                            rellenar(0);
                            rellenar(-1);
                        },
                    error: function(error) {
                         console.log(error);
                    }
            });
        }
        function rellenar(z)
        {
            	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,z:z,tipo:"tablas"},
                    success: function(response) {
                            console.log(response);
                            var respon2 = response.trim();
                            var s = respon2.split("$");
                            for(var i = 0 ; i < s.length-1; i++)
                            {
                                console.log(s[i]);
                                var r = s[i].split("#");
                                if (r[1] == "0")
                                {
                                $("#"+r[0]).css("background","blue");
                                }
                                else
                                {
                                $("#"+r[0]).css("background","red");
                                }
                            }

                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
    }
        function disparo()
        {
            var x = $("#disparox").val();

            var y = letra($("#disparoy").val());
            alert(y);
            alert(letra('D'));
            var z = $("$disparoz").val();
            var zt = ["barco","avione","satelite"];
            var z2 = "";
            if ( z >= 0)
            {
             z2 = zt[z];
            }
            else
            {
                z2 = "submarino";
            }
            var sx = x.toString()
            var sy = y.toString()
            	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,z:z,tipo:"disparo",x:x,y:y},
                    success: function(response) {
                        $("#T"+sx+z2+sy).css("background","red");
                         $("#add").attr("disabled",true);
                            console.log(response);
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
        function crearTablas(tipo)
        {
            var tabla = "<table class='table table-bordered'>";
              var letras = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]; 
            for (var ty = 0 ; ty <= y ; ty ++)
            {
                tabla = tabla + "<tr>"
                for(var tx=0 ; tx <= x ; tx++)
                {
                    var txs = tx.toString();
                    var tys = ty.toString();
                    if (tx ==0)
                    {
                       tabla = tabla + "<td id ='" +txs+tipo+tys+"'>"+tys+"</td>";
                    }
                    else
                    {
                    if(ty == 0)
                    {
                        tabla = tabla + "<td id ='" +txs+tipo+tys+"'>"+letras[tx]+"</td>";
                    }
                    else
                    {
                        tabla = tabla + "<td id ='" +txs+tipo+tys+"'></td>";
                    }
                }
                }
                tabla = tabla+ "</tr>";
             }   
             tabla = tabla + "</table>";
            $("#"+tipo+"sMios").html(tabla);
            
        }
        function crearTablasEnemigas(tipo)
        {
            var letras = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]; 
            var tabla = "<table class='table table-bordered'>";
            for (var ty = 0 ; ty <= y ; ty ++)
            {
                tabla = tabla + "<tr>"
                for(var tx=0 ; tx <= x ; tx++)
                {
                    var txs = tx.toString();
                    var tys = ty.toString();
                    if ( tx == 0)
                    {
                        tabla = tabla + "<td id ='T" +txs+tipo+tys+"'>"+tys+"</td>";
                    
                    }
                    else
                    {
                        if (ty == 0)
                    {
                        tabla = tabla + "<td id ='T" +txs+tipo+tys+"'>"+letras[tx]+"</td>";
                    }
                    else
                    {
                    tabla = tabla + "<td id ='T" +txs+tipo+tys+"'></td>";
                    }
                    }
                    
                }
                tabla = tabla+ "</tr>";
             }   
             tabla = tabla + "</table>";
            $("#"+tipo+"sEnemigo").html(tabla);
        }
        function getGame()
        {
        
          $.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,tipo:"getGame"},
                    success: function(response) {
                            //console.log(response);
                            var res = response.split(",");
                            x = res[5];
                            y = res[6];
                            console.log("Ekecuto");
                            crearTablas("satelite");
                            crearTablas("avione");
                            crearTablas("barco");
                            crearTablas("submarino");  
                            crearTablasEnemigas("satelite");
                            crearTablasEnemigas("avione");
                            crearTablasEnemigas("barco");
                            crearTablasEnemigas("submarino")
                            rellenar(1);
                            rellenar(2);
                            rellenar(0);
                            rellenar(-1);
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});  
        }
        function revisar()
        {
            	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,tipo:"enjuego"},
                    success: function(response) {
                            console.log(response);
                            var respon2 = response.trim();
                            if (respon2 === "True")
                            {
                                enjuego = true;
                               // alert("entrue");
                            }
                            else
                            {
                                enjuego = false;
                                //alert("enfalse");
                            }
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }

        function ver()
        {
            var x = letra($("#disparox").val());
            var y = $("#disparoy").val();
            var z = $("#disparoz").val();
             var zt = ["barco","avione","satelite"];
            var z2 = "";
            if ( z >= 0)
            {
             z2 = zt[z];
            }
            else
            {
                z2 = "submarino";
            }
            var sx = x.toString();
            var sy = y.toString();
            	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,z:z,tipo:"disparo",x:x,y:y},
                    success: function(response) {
                            console.log(response);
                            $("#T"+sx+z2+sy).css("background","red");
                            $("#add").attr("disabled",true);
                            
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
         function turnoA()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,tipo:"enturno"},
                    success: function(response) {
                           // console.log(response);
                           var respon2 = response.trim();
                            if (respon2 === "True")
                            {
                                turno = true;
                                 rellenar(1);
                                rellenar(2);
                                rellenar(0);
                                rellenar(-1);
                               // alert("entrue");
                            }
                            else
                            {
                                turno = false;
                                //alert("enfalse");
                            }
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
          function gane()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,tipo:"gane"},
                    success: function(response) {
                           // console.log(response);
                           var respon2 = response.trim();
                            if (respon2 === "True")
                            {
                                alert("gane");
                                clearInterval(refreshIntervalId);
                               // alert("entrue");
                            }
                            else
                            {
                                //turno = false;
                                //alert("enfalse");
                            }
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
         function getcubo()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,tipo:"getcubo"},
                    success: function(response) {
                           // console.log(response);
                         $("#respuestaM").html("<img src=\"data:image/png;base64,"+response+"\">");
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
         function getA()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,tipo:"geta"},
                    success: function(response) {
                           // console.log(response);
                         $("#respuestaM").html("<img src=\"data:image/png;base64,"+response+"\">");
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
            function getF()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,tipo:"getf"},
                    success: function(response) {
                           // console.log(response);
                         $("#respuestaM").html("<img src=\"data:image/png;base64,"+response+"\">");
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
             function inicial()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {usuario:usuario,tipo:"getcuboinicial"},
                    success: function(response) {
                           // console.log(response);
                         $("#respuestaM").html("<img src=\"data:image/png;base64,"+response+"\">");
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
               function arbol()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {tipo:"getusuarios"},
                    success: function(response) {
                           // console.log(response);
                         $("#respuestaM").html("<img src=\"data:image/png;base64,"+response+"\">");
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
              function arbolE()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {tipo:"getespejo"},
                    success: function(response) {
                           // console.log(response);
                         $("#respuestaM").html("<img src=\"data:image/png;base64,"+response+"\">");
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
                   function ArbolDatos()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {tipo:"estadisticas"},
                    success: function(response) {
                           // console.log(response);
                         $("#respuestaM").html(response);
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
        function letra( letra1)
        {
            var letrag = letra1.toString(); 
            var letras = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];  
        for (var i = 0 ; i < letras.length ; i++)
        {
            if (letras[i] == letrag)
            {
                return i;
            }
        }
        return 255;
        }
              function setOrden()
        {
                   	$.ajax({	
                    url : '/cliente/llamarpython',
                    type: "POST",
                    data : {tipo:"setOrden",or:$("#ordenarb").val()},
                    success: function(response) {
                           // console.log(response);
                         $("#respuestaM").html(response);
                    },
                    error: function(error) {
                         console.log(error);
                    }
	});
        }
    </script>
    <body>
        
       
        <%
            if (strUsuarioActual.equals("Admin"))
                    {
        %>
        		<form action="subir" enctype="MULTIPART/FORM-DATA" method="post">
			<input type="file" name="archivo_parametro" /><br/>
                        <select name="selecciona">
                            <option>Usuarios</option>
                            <option>Juego</option>
                            <option>naves</option>
                            <option>JuegoActual</option>
                            <option>contactos</option>
                            <option>historial</option>
                        </select>
			<input type="submit" value="Upload" />
		</form>
                        Ordenar B por : <select id="ordenarb">
                            <option value="x">x</option>
                            <option value="y">y</option>
                            <option value="tiro">Tiro</option>
                            <option value="res">Resultado</option>
                            <option value="emisor">Emisor</option>
                            <option value="receptor">receptor</option>
                            <option value="fecha">fecha</option>
                            <option value="tiempo">tiempo</option>
                            <option value="NoTiro">Numero de Tiro</option>
                            <option value="tipo">Tipo Nave</option>
                           
                        </select>
                        <input type="button" onclick="setOrden()">
                <input type="button" onclick="letra('D')">
                <div class="row">
                    
                    <div class="col-md-4"><br>
                        <button onclick="listarusuarios()">Cargar usuarios</button>
                        <select id="listausuarios"></select>
                    </div>
                    <div class="col-md-4"><button onclick="eliminarus()">Eliminar Usuario</button></div>
         
                    <div class="col-md-4">Nueva Password<input id="contranueva">
                                    <button onclick="editarus()">Editar Usuario</button>
                    </div>
                   
                </div>
                 <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal" onclick="arbol()">Arbol Usuarios</button>
      <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal" onclick="arbolE()">Arbol Espejo</button>
      <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal" onclick="ArbolDatos()">Arbol Datos</button>
      <% } %>
      <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal" onclick="getcubo()">Actual</button>
      <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal" onclick="inicial()">CuboInicial</button>
      <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal" onclick="getA()">Tiros Acertados</button>
      <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal" onclick="getF()">Tiros Fallados</button>
      <div id="turnoDiv"></div>
      Disparo x <input id ="disparox">
      Disparo y <input id ="disparoy">
      <select id="disparoz">
          <option value="2">Satelite</option>
          <option value="1">Avion</option>
          <option value="0">Barco</option>
          <option value="-1">Submarino</option>
      </select>
      <button onclick="ver()" id="gt">Boom</button>
      <div >
        Fila:  <input id="adfila">
        Columna:  <input id="adcol">
          <select id="adnave">
          <option value="1">Satelite</option>
          <option value="2">Avion</option>
          <option value="3">Barco</option>
          <option value="4">Submarino</option>
        </select>
        Modo :  <input id="modo">
           <select id="direct">
          <option value="1">horizontal</option>
          <option value="2">Vertical</option>
          
        </select>
        <button onclick="AgregarNave()" id="add">Agregar Nave</button>
      </div>
                <div class="row">
                    
                    <div class="col-md-6">
                 <h1 class="display-4">Tu tablero</h1>     
                <h1 class="display-4"> Satelites </h1>       
                <div id="satelitesMios"></div>
                <h1 class="display-4"> Aviones </h1> 
                <div id="avionesMios"></div>
                <h1 class="display-4"> Barcos </h1> 
                <div id="barcosMios"></div>
                <h1 class="display-4"> Submarino </h1> 
                <div id="submarinosMios"></div>
                    </div>
                    <div class="col-md-6">
                        <h1 class="display-4">ENEMIGP !! prro!</h1>     
                <h1 class="display-4"> Satelites Enemigos !</h1>       
                <div id="satelitesEnemigo"></div>
                <h1 class="display-4"> Aviones Enemigos!</h1> 
                <div id="avionesEnemigo"></div>
                <h1 class="display-4"> Barcos Enemigos! </h1> 
                <div id="barcosEnemigo"></div>
                <h1 class="display-4"> Submarino Enemigos!</h1> 
                <div id="submarinosEnemigo"></div>
                    </div>
                </div>
        
      <style>
          #myModal{
              position:absolute;
overflow:scroll;
          }
      </style>
        <div id="myModal" class="modal fade" role="dialog">
            
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">Reportes</h4>
      </div>
      <div class="modal-body">
        <div id="respuestaM"></div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>

  </div>
</div>
    </body>
</html>
