import SearchResult from '../SearchResult/SearchResult';
import classes from './SearchResults.module.css';
import Modal from '../FlatModal/FlatModal';
import { useState } from 'react';
import PredictModal from '../PredicitonModal/PredictionModal';

const SearchResults = ({ results }) => {
  const [modalOpened, setModalOpened] = useState(false);
  const [predictionModalOpened, setPredicitonModalOpened] = useState(false);
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

  const closePredictionModalHandler = () => {
    setPredicitonModalOpened(false);
  }

  return (
    <div className={classes.wrapper}>
      {results.map((result) => (
        <div className={classes.result}>
          <SearchResult key={result.id} searchResult={result} onClick={resultClickHandler} />
        </div>
      ))}


      <button
        className={classes.predictBtn}
        onClick={() => setPredicitonModalOpened((prev) => !prev)}
      >Price AI</button>


      {modalOpened && <Modal flat={modalData} onClose={closeModalHandler} />}
      {predictionModalOpened && <PredictModal onClose={closePredictionModalHandler} />}

    </div>
  )
}

export default SearchResults;