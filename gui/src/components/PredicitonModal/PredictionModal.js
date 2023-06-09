import classes from './PredictionModal.module.css';
import { useState } from 'react';
import ReactDOM from 'react-dom';

const Modal = (props) => {
  const [price, setPrice] = useState(null);
  const [error, setError] = useState(null);
  const [rooms, setRooms] = useState(null);
  const [area, setArea] = useState(null);

  const closeModalHandler = () => {
    props.onClose();
  }

  const predictPrice = (event) => {
    event.preventDefault();
    console.log('predict price clicked');
    fetch('http://localhost:8070/price_prediction?' + new URLSearchParams({rooms: rooms, area: area}), {mode: 'no-cors'})
      .then(response => response.json())
      .then(data => setPrice(data.predicted_price))
      .catch(error => setError(error));
  }

  const roomsChangeHandler = (event) => {
    setRooms(event.target.value);
  }

  const areaChangeHandler = (event) => {
    setArea(event.target.value);
  }

  return (
    <div className={classes.wrapper}>
      <p className={classes.title}>Poznaj cenę wymarzonego mieszkania</p>
      <p className={classes.exitButton} onClick={closeModalHandler}>x</p>
      <form className={classes.form} onSubmit={predictPrice}>
        <div className={classes.formControl}>
          <label htmlFor="rooms">Pokoje</label>
          <input
            type="number"
            id="rooms"
            name="rooms"
            onChange={roomsChangeHandler}
            value={rooms}
            placeholder="3"
            min={1}
            max={10}
            required
          />
        </div>
        <div className={classes.formControl}>
          <label htmlFor="area">Powierzchnia</label>
          <input
            type="number"
            id="area"
            name="area"
            onChange={areaChangeHandler}
            value={area}
            placeholder="65"
            min={10}
            max={800}
            required
          />
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