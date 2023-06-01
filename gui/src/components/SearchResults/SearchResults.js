import SearchResult from '../SearchResult/SearchResult';
import classes from './SearchResults.module.css';
import Modal from '../FlatModal/FlatModal';
import { useState } from 'react';

const SearchResults = ({ results }) => {
  const [modalOpened, setModalOpened] = useState(false);

  const resultClickHandler = (searchResult) => {
    console.log('result clicked');
    console.log(searchResult);

    setModalOpened((prev) => !prev);
  }

  const closeModalHandler = () => {
    setModalOpened(false);
  }

  return (
    <div className={classes.wrapper}>
      {results.map((result) => (
        <div className={classes.result}>
          <SearchResult searchResult={result} onClick={resultClickHandler} />
        </div>
      ))}

      {modalOpened && <Modal flat={results[0]} onClose={closeModalHandler} />}
    </div>
  )
}

export default SearchResults;