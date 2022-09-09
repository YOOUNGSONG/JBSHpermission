<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>전달받은 데이터</h1>
        <ul>
            <li>학번: <%= request.getParameter("num") %></li>
            <li>이름: <%= request.getParameter("name") %></li>
        </ul>
    </body>
</html>
