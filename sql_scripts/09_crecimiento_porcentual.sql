USE Northwind

WITH VentasMensuales AS (
	SELECT 
	FORMAT(o.fecha, 'yyyy-MM') AS Mes,
	SUM(d.UnitPrice * d.Quantity) AS TotalVenta
	FROM DetalleOrden d
	INNER JOIN Orden o ON d.ordenID = o.ordenID
	GROUP BY FORMAT(o.fecha, 'yyyy-MM'))
SELECT
Mes, 
ROUND(TotalVenta, 2) AS TotalVenta,
ROUND(
	(TotalVenta - LAG(TotalVenta) OVER (ORDER BY Mes)) 
	/ LAG(TotalVenta) OVER (ORDER BY Mes) * 100, 2) AS CrecimientoPorcentual
FROM VentasMensuales
ORDER BY Mes