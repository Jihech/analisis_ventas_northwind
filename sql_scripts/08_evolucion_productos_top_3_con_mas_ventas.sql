USE Northwind

WITH TopProducts AS (
    SELECT TOP 3
        p.nombre
    FROM DetalleOrden d
    INNER JOIN Producto p ON d.productoID = p.productoID
    GROUP BY p.nombre
    ORDER BY SUM(d.UnitPrice * d.Quantity) DESC)
SELECT 
    FORMAT(o.fecha, 'yyyy-MM') AS Mes,
    p.nombre,
    ROUND(SUM(d.UnitPrice * d.Quantity), 2) AS TotalVenta
FROM DetalleOrden d
INNER JOIN Producto p ON d.productoID = p.productoID
INNER JOIN Orden o ON d.ordenID = o.ordenID

WHERE p.nombre IN (SELECT nombre FROM TopProducts)
GROUP BY FORMAT(o.fecha, 'yyyy-MM'), p.nombre
ORDER BY Mes, p.nombre
