import SearchResult from '../SearchResult/SearchResult';
import classes from './SearchResults.module.css';
import Modal from '../FlatModal/FlatModal';
import { useState } from 'react';

const SearchResults = ({ results }) => {
  const [modalOpened, setModalOpened] = useState(false);
  const [modalData, setModalData] = useState(null);

  const resultClickHandler = (searchResult) => {
    console.log('result clicked');
    console.log(searchResult);
    setModalData(searchResult);
    setModalOpened((prev) => !prev);
  }

  const closeModalHandler = () => {
    setModalOpened(false);
  }

  return (
    <div className={classes.wrapper}>
      {results.map((result) => (
        <div className={classes.result}>
          <SearchResult key={result.id} searchResult={result} onClick={resultClickHandler} />
        </div>
      ))}

      {modalOpened && <Modal flat={modalData} onClose={closeModalHandler} />}
    </div>
  )
}

export default SearchResults;