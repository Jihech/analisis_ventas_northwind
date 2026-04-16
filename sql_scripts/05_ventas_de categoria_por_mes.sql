USE Northwind

SELECT 
FORMAT(o.fecha, 'yyyy-MM') AS Mes,
c.nombre,
ROUND(SUM(d.UnitPrice * d.Quantity), 2) AS TotalVenta
FROM DetalleOrden d
INNER JOIN Producto p ON d.productoID = p.productoID
INNER JOIN Categoria c ON p.categoriaID = c.categoriaID
INNER JOIN Orden o ON d.ordenID = o.ordenID
GROUP BY FORMAT(o.fecha, 'yyyy-MM'), c.nombre
ORDER BY Mes, c.nombre