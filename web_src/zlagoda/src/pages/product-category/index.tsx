import ProductCategoryList from "@/app/components/product-category/ProductCategoryList";
import {Dialog, DialogContent} from "@mui/material";
import {ReactElement, useState} from "react";
import ProductCategoryUpsert from "@/app/components/product-category/ProductCategoryUpsert";
import BasePage from "@/app/components/common/pages/BasePage";

export default function ProductCategoryListPage() {
  const [modalContent, setModalContent] = useState<ReactElement | null>(null);

  function closeModal() {
    setModalContent(null);
  }

  function openModal(content: ReactElement) {
    setModalContent(content);
  }

  function onSave(callback: () => void): () => void {
    return () => {
      callback();
      closeModal();
    };
  }

  function create(callback: () => void) {
    openModal(<ProductCategoryUpsert initialId={null} onError={closeModal} cancel={closeModal} onSave={onSave(callback)} />);
  }

  function update(id: number, callback: () => void) {
    openModal(<ProductCategoryUpsert initialId={id} onError={closeModal} cancel={closeModal} onSave={onSave(callback)} />);
  }

  return (
    <BasePage>
      <ProductCategoryList
        create={create}
        update={update}
      />
      <Dialog
        open={modalContent != null}
        onClose={closeModal}
      >
        <DialogContent sx={{ padding: 4 }}>
          {modalContent ?? <div></div>}
        </DialogContent>
      </Dialog>
    </BasePage>
  );
}
