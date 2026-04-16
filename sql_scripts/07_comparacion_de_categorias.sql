USE Northwind

SELECT 
FORMAT(o.fecha, 'yyyy-MM') AS Mes,
ROUND(SUM(CASE WHEN c.nombre = 'Beverages' THEN d.UnitPrice * d.Quantity ELSE 0 END), 2) AS Bebidas,
ROUND(SUM(CASE WHEN c.nombre = 'Condiments' THEN d.UnitPrice * d.Quantity ELSE 0 END), 2) AS Condimentos,
ROUND(SUM(CASE WHEN c.nombre = 'Produce' THEN d.UnitPrice * d.Quantity ELSE 0 END), 2) AS Frutas_Verduras,
ROUND(SUM(CASE WHEN c.nombre = 'Grains/Cereals' THEN d.UnitPrice * d.Quantity ELSE 0 END), 2) AS Granos_Cereales

FROM DetalleOrden d
INNER JOIN Producto p ON d.productoID = p.productoID
INNER JOIN Categoria c ON p.categoriaID = c.categoriaID
INNER JOIN Orden o ON d.ordenID = o.ordenID

WHERE c.nombre IN ('Grains/Cereals', 'Condiments', 'Produce', 'Beverages')
GROUP BY FORMAT(o.fecha, 'yyyy-MM')
ORDER BY Mes ASC