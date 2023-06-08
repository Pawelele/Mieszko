import classes from './PredictionModal.module.css';
import { useState } from 'react';
import ReactDOM from 'react-dom';

const Modal = (props) => {
  const [price, setPrice] = useState(null);
  const [error, setError] = useState(null);

  const closeModalHandler = () => {
    props.onClose();
  }

  const predictPrice = () => {
    console.log('predict price clicked');
    fetch('http://localhost:5000/predict', {})
      .then(response => response.json())
      .then(data => setPrice(data.price))
      .catch(error => setError(error));
  }

  return (
    <div className={classes.wrapper}>
      <p className={classes.title}>Poznaj cenę wymarzonego mieszkania</p>
      <p className={classes.exitButton} onClick={closeModalHandler}>x</p>
      <form className={classes.form}>
        <div className={classes.formControl}>
          <label for="rooms">Cena</label>
          <input type="number" id="rooms" name="price" placeholder="3" min={1} max={10} required/>
        </div>
        <div className={classes.formControl}>
          <label for="area">Powierzchnia</label>
          <input type="number" id="area" name="area" placeholder="65" min={10} max={800} required/>
        </div>
        <button className={classes.predictButton}>Poznaj cenę</button>
      </form>

      <div className={classes.price}>
        {price && <h2>{price} zł</h2>}
      </div>
      {{error} && <p>{error}</p>}
    </div>
  )
}

const PredictModal = (props) => {
  return (
    <>
      {ReactDOM.createPortal(<Modal onClose={props.onClose} />, document.getElementById('modal-root'))}
    </>
  )
}

export default PredictModal;