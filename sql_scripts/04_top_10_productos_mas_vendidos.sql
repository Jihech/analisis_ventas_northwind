USE Northwind

SELECT TOP 10
p.nombre,
SUM(d.Quantity) AS CantidadVendida
FROM DetalleOrden d 
INNER JOIN Producto p ON d.productoID = p.productoID
GROUP BY p.nombre
ORDER BY CantidadVendida DESC
