USE Northwind

SELECT	
FORMAT(o.fecha, 'yyyy-MM') AS Mes,
ROUND(SUM(d.UnitPrice * d.Quantity), 2) AS TotalVentas
FROM Orden o INNER JOIN DetalleOrden d ON o.ordenID = d.ordenID
GROUP BY FORMAT(o.fecha, 'yyyy-MM')
ORDER BY Mes