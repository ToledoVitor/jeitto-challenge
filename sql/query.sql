SELECT Cliente, count(*) as NumPedidos
FROM Pedidos
GROUP BY Cliente
HAVING NumPedidos > 5
