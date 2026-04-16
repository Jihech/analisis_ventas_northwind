USE Northwind

SELECT TOP 10
p.nombre,
ROUND(SUM(d.UnitPrice * d.Quantity), 2) AS TotalVenta
FROM DetalleOrden d
INNER JOIN Producto p ON d.productoID = p.productoID
GROUP BY p.nombre
ORDER BY TotalVenta DESC