WITH country_invoices AS (
    SELECT
        c.country_name,
        COUNT(i.id) AS total_invoices,
        AVG(i.total_price) AS avg_amount
    FROM
        country c
    JOIN
        city ct ON c.id = ct.country_id
    JOIN
        customer cu ON ct.id = cu.city_id
    JOIN
        invoice i ON cu.id = i.customer_id
    GROUP BY
        c.country_name
)


, overall_avg AS (
    SELECT
        AVG(i.total_price) AS overall_avg_amount
    FROM
        invoice i
)


SELECT
    ci.country_name,
    ci.total_invoices,
    ROUND(ci.avg_amount, 6) AS avg_amount
FROM
    country_invoices ci
CROSS JOIN
    overall_avg oa
WHERE
    ci.avg_amount > oa.overall_avg_amount
ORDER BY
    ci.country_name ASC;


WITH country_invoices AS (
    SELECT
        c.country_name,
        COUNT(i.id) AS total_invoices,
        AVG(i.total_price) AS avg_amount
    FROM
        country c
    JOIN
        city ct ON c.id = ct.country_id
    JOIN
        customer cu ON ct.id = cu.city_id
    JOIN
        invoice i ON cu.id = i.customer_id
    GROUP BY
        c.country_name
),
overall_avg AS (
    SELECT
        AVG(i.total_price) AS overall_avg_amount
    FROM
        invoice i
)
SELECT
    ci.country_name,
    ci.total_invoices,
    ROUND(ci.avg_amount, 6) AS avg_amount
FROM
    country_invoices ci
CROSS JOIN
    overall_avg oa
WHERE
    ci.avg_amount > oa.overall_avg_amount
ORDER BY
    ci.country_name ASC;
