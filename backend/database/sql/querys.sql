-- Último Trimestre (outubro a dezembro de 2024)
SELECT 
    o.razao_social,
    SUM(p.vl_saldo_final) AS despesas_totais
FROM 
    procedimentos p
JOIN 
    operadoras o ON p.reg_ans = o.registro_ans
WHERE 
    p.descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE%'
    AND p.data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY 
    o.razao_social
ORDER BY 
    despesas_totais DESC
LIMIT 10;

-- Último Ano (2024 inteiro)
SELECT 
    o.razao_social,
    SUM(p.vl_saldo_final) AS despesas_totais
FROM 
    procedimentos p
JOIN 
    operadoras o ON p.reg_ans = o.registro_ans
WHERE 
    p.descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE%'
    AND p.data BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY 
    o.razao_social
ORDER BY 
    despesas_totais DESC
LIMIT 10;