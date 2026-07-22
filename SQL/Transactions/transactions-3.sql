DO $$
DECLARE
    v_bill_id INTEGER := 1;      -- Receipt to return
    rec RECORD;
BEGIN

    -- Verify the receipt exists
    IF NOT EXISTS (
        SELECT 1
        FROM bills
        WHERE bill_id = v_bill_id
    ) THEN
        RAISE EXCEPTION 'Receipt does not exist.';
    END IF;

    -- Verify it has not already been returned
    IF EXISTS (
        SELECT 1
        FROM bills
        WHERE bill_id = v_bill_id
          AND status = 'RETURNED'
    ) THEN
        RAISE EXCEPTION 'Receipt has already been returned.';
    END IF;

    -- Increase stock for each purchased product
    FOR rec IN
        SELECT product_id, quantity
        FROM bill_items
        WHERE bill_id = v_bill_id
    LOOP

        UPDATE products
        SET stock = stock + rec.quantity
        WHERE product_id = rec.product_id;

    END LOOP;

    -- Mark receipt as returned
    UPDATE bills
    SET status = 'RETURNED'
    WHERE bill_id = v_bill_id;

END $$;