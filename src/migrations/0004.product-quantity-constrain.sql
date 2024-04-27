ALTER TABLE product
ADD CONSTRAINT non_negative_quantity CHECK ( quantity >= 0 )