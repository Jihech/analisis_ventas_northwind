USE Northwind

WITH TopCategorias AS (
	SELECT TOP 5
	c.nombre
	FROM DetalleOrden d
	INNER JOIN Producto p ON d.productoID = p.productoID
	INNER JOIN Categoria c ON p.categoriaID = c.categoriaID
	GROUP BY c.nombre
	ORDER BY SUM(d.UnitPrice * d.Quantity) DESC)
SELECT
FORMAT(o.fecha, 'yyyy-MM') AS Mes, 
c.nombre AS NombreCategoria,
ROUND(SUM(d.UnitPrice * d.Quantity), 2) AS TotalVenta
FROM DetalleOrden d
INNER JOIN Producto p ON d.productoID = p.productoID
INNER JOIN Categoria c ON p.categoriaID = c.categoriaID
INNER JOIN Orden o ON d.ordenID = o.ordenID

WHERE c.nombre IN (SELECT c.nombre FROM TopCategorias)
GROUP BY FORMAT(o.fecha, 'yyyy-MM'), c.nombre
ORDER BY Mes, NombreCategoria