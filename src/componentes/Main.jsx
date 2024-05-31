import React, { useState } from 'react';
import ReactLogo from '../assets/imagen.jpeg';

export default function Main() {
  const [formData, setFormData] = useState({
    radius_mean: '',
    texture_mean: '',
    perimeter_mean: '',
    area_mean: '',
    smoothness_mean: '',
    compactness_mean: '',
    concavity_mean: '',
    concave_points_mean: '',
    symmetry_mean: '',
    fractal_dimension_mean: '',
    radius_se: '',
    texture_se: '',
    perimeter_se: '',
    area_se: '',
    smoothness_se: '',
    compactness_se: '',
    concavity_se: '',
    concave_points_se: '',
    symmetry_se: '',
    fractal_dimension_se: '',
    radius_worst: '',
    texture_worst: '',
    perimeter_worst: '',
    area_worst: '',
    smoothness_worst: '',
    compactness_worst: '',
    concavity_worst: '',
    concave_points_worst: '',
    symmetry_worst: '',
    fractal_dimension_worst: ''
  });

  const [showTextInput, setShowTextInput] = useState(true); // Estado para manejar la caja visible
  const [pdfFile, setPdfFile] = useState(null); // Estado para almacenar el archivo PDF

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleFileChange = (e) => {
    setPdfFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (showTextInput) {
      console.log(formData);
    } else {
      console.log(pdfFile);
    }
  };

  const toggleInputType = () => {
    setShowTextInput(!showTextInput);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 relative ">
      <div className="flex flex-col items-center justify-center w-full h-full relative">
        <img className="w-full h-auto max-h-screen object-contain" src={ReactLogo} alt="React Logo" />
        <div className="absolute z-10 top-1/2 transform -translate-y-1/2 text-center">
          <h1 className="text-6xl font-bold mb-8">"Slogan"</h1>
          <button className="bg-blue-500 text-white py-2 px-4 rounded-lg text-xl">Start</button>
        </div>
      </div>
      <div className="relative z-10 mb-6 flex flex-col items-center w-full max-w-4xl p-8 bg-white bg-opacity-75 rounded-lg shadow-lg mt-8">
        <button onClick={toggleInputType} className="bg-blue-500 text-white py-2 px-4 rounded mb-4">
          {showTextInput ? 'Switch to PDF Input' : 'Switch to Text Input'}
        </button>
        <form onSubmit={handleSubmit} className="w-full">
          {showTextInput ? (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {Object.keys(formData).map((key) => (
                <div key={key} className="flex flex-col">
                  <label htmlFor={key} className="mb-2 capitalize">{key.replace('_', ' ')}</label>
                  <input
                    type="text"
                    id={key}
                    name={key}
                    value={formData[key]}
                    onChange={handleChange}
                    className="p-2 border border-gray-300 rounded"
                    required
                  />
                </div>
              ))}
            </div>
          ) : (
            <div className="flex flex-col items-center">
              <label htmlFor="pdfFile" className="mb-2">Upload PDF</label>
              <input
                type="file"
                id="pdfFile"
                name="pdfFile"
                accept="application/pdf"
                onChange={handleFileChange}
                className="p-2 border border-gray-300 rounded"
                required
              />
            </div>
          )}
          <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded mt-4">
            Enviar
          </button>
        </form>
      </div>
    </div>
  );
}