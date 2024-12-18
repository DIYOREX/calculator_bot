CREATE TABLE CRUD (
                      id SERIAL PRIMARY KEY,
                      name VARCHAR(100),
                      age INT,
                      address VARCHAR(255)
);

CREATE OR REPLACE FUNCTION create_person(p_name VARCHAR, p_age INT, p_address VARCHAR) RETURNS VOID AS $$
BEGIN
    INSERT INTO CRUD (name, age, address)
    VALUES (p_name, p_age, p_address);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_persons()
    RETURNS TABLE(id INT, name VARCHAR, age INT, address VARCHAR)
AS $$
BEGIN
    RETURN QUERY
        SELECT CRUD.id, CRUD.name, CRUD.age, CRUD.address FROM CRUD;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_person(p_id INT, p_age INT, p_address VARCHAR) RETURNS VOID AS $$
BEGIN
    UPDATE CRUD
    SET age = p_age, address = p_address
    WHERE id = p_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_person(p_id INT) RETURNS VOID AS $$
BEGIN
    DELETE FROM CRUD
    WHERE id = p_id;
END;
$$ LANGUAGE plpgsql;

SELECT create_person('Ali', 25, 'Toshkent');
SELECT create_person('Vali', 30, 'Samarqand');

SELECT * FROM get_persons();

SELECT update_person(1, 26, 'new_york');

SELECT delete_person(2);
