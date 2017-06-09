<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page session="false" %>
<html>
<head>
	<title>Home</title>
</head>
<body>
<h1>
	Hello world!  
</h1>

<P>  The time on the server is ${serverTime}. </P>
<table border="1">
		<tr><th>date</th><th>website</th><<th>visits</th></tr>
		<c:choose>
			<c:when test="${empty websiteData}">
				<!-- if personData is empty, show "No data" -->
				<tr><td colspan="4" align="center">No Data</td></tr>
			</c:when>
			<c:otherwise>
				<!-- if it's not empty, show the data-->
				<c:forEach items="${websiteData}" var="websiteData">
					<tr>
						<td>${websiteData.date}</td>
						<td>${websiteData.website}</td>
						<td>${websiteData.visits}</td>
					</tr>
				</c:forEach>
			</c:otherwise>
		</c:choose>
	</table>
</body>
</html>
