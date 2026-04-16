USE Northwind

SELECT 
c.nombre,
ROUND(SUM(d.UnitPrice * d.Quantity), 2) AS TotalVenta
FROM DetalleOrden d 
INNER JOIN Producto p ON d.productoID = p.productoID
INNER JOIN Categoria c ON p.categoriaID = c.categoriaID
GROUP BY c.nombre
ORDER BY TotalVenta DESC