DO $$
DECLARE
    v_user INTEGER := 1;
    v_bill INTEGER;
    v_stock INTEGER;
BEGIN

    -- Check if user exists
    IF NOT EXISTS (
        SELECT 1
        FROM users
        WHERE user_id = v_user
    ) THEN
        RAISE EXCEPTION 'User does not exist';
    END IF;

    -- Check stock for Laptop (Product 1)
    SELECT stock
    INTO v_stock
    FROM products
    WHERE product_id = 1;

    IF v_stock < 2 THEN
        RAISE EXCEPTION 'Insufficient stock for Laptop';
    END IF;

    -- Check stock for Mouse (Product 2)
    SELECT stock
    INTO v_stock
    FROM products
    WHERE product_id = 2;

    IF v_stock < 3 THEN
        RAISE EXCEPTION 'Insufficient stock for Mouse';
    END IF;

    -- Create Bill
    INSERT INTO bills(user_id,total)
    VALUES (v_user,2475)
    RETURNING bill_id INTO v_bill;

    -- Insert bill items
    INSERT INTO bill_items(bill_id,product_id,quantity,price)
    VALUES
    (v_bill,1,2,1200),
    (v_bill,2,3,25);

    -- Update inventory
    UPDATE products
    SET stock = stock - 2
    WHERE product_id = 1;

    UPDATE products
    SET stock = stock - 3
    WHERE product_id = 2;

END $$;