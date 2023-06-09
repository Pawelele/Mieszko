import classes from './PredictionModal.module.css';
import { useState } from 'react';
import ReactDOM from 'react-dom';
import HashLoader from "react-spinners/HashLoader";

const override = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  display: "block",
  margin: "0 auto",
  borderColor: "red",
};

const Modal = (props) => {
  const [price, setPrice] = useState(null);
  const [error, setError] = useState(null);
  const [rooms, setRooms] = useState(null);
  const [area, setArea] = useState(null);
  const [loading, setLoading] = useState(false);

  const closeModalHandler = () => {
    props.onClose();
  }

  const predictPrice = (event) => {
    event.preventDefault();
    setLoading(true);
    fetch('http://127.0.0.1:8070/price_prediction?' + new URLSearchParams({rooms: rooms, area: area}))
      .then(response => {
        setLoading(false);
        return response.json()
        })
      .then(data => {
        const price = data.predictedPrice.toFixed(2);
        setPrice(price);
      })
      .catch(error => {
        setLoading(false);
        setError(error)
      });
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
        <HashLoader
          color={'#00FFEF'}
          loading={loading}
          cssOverride={override}
          size={90}
          aria-label="Loading Spinner"
          data-testid="loader"
        />
        {price && <h2>{price} zł</h2>}
      </div>
      {{error} && <p>{error}</p>}
    </div>
  )
}

const Backdrop = (props) => {
  return (
    <div className={classes.backdrop} onClick={props.onClose}></div>
  )
}

const PredictModal = (props) => {
  return (
    <>
      {ReactDOM.createPortal(<Modal onClose={props.onClose} />, document.getElementById('modal-root'))}
      {ReactDOM.createPortal(<Backdrop onClose={props.onClose} />, document.getElementById('backdrop-root'))}
    </>
  )
}

export default PredictModal;