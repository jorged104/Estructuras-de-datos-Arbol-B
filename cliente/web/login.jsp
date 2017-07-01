<%-- 
    Document   : login
    Created on : Jun 26, 2017, 10:23:35 AM
    Author     : Jorge
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
<body>
 <%
 String user = request.getParameter("usuario");
 String pass = request.getParameter("password");
 if(user.equals("denisse") && pass.equals("123")){
 out.println("Hola Denisse");
 }else{
 out.println("Desconocido");
 }
 PeticionPost post = new PeticionPost("");
 String res = post.getRespueta();
 
 %>
 <a href="data:;base64,<% out.println(res); %>">Vinculo</a>

</body>
</html>
