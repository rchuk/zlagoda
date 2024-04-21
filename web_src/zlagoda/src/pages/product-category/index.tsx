import ProductCategoryList from "@/app/components/product-category/ProductCategoryList";
import {Box, Dialog} from "@mui/material";
import {ReactElement, useState} from "react";
import ProductCategoryUpsert from "@/app/components/product-category/ProductCategoryUpsert";

export default function ProductCategoryListPage() {
  const [modalContent, setModalContent] = useState<ReactElement | null>(null);

  function closeModal() {
    setModalContent(null);
  }

  function openModal(content: ReactElement) {
    setModalContent(content);
  }

  function create(callback: () => void) {
    openModal(<ProductCategoryUpsert initialId={null} onError={closeModal} cancel={closeModal} onSave={callback} />);
  }

  function update(id: number, callback: () => void) {
    openModal(<ProductCategoryUpsert initialId={id} onError={closeModal} cancel={closeModal} onSave={callback} />);
  }

  return (
    <Box>
      <ProductCategoryList
        create={create}
        update={update}
      />
      <Dialog
        open={modalContent != null}
        onClose={closeModal}
      >
        {modalContent ?? <div></div>}
      </Dialog>
    </Box>
  );
}
