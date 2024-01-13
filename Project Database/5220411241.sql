-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 13, 2024 at 05:58 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411241`
--

-- --------------------------------------------------------

--
-- Table structure for table `karya_seni_2d`
--

CREATE TABLE `karya_seni_2d` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `teknik` varchar(255) NOT NULL,
  `pembuat` varchar(255) DEFAULT NULL,
  `panjang` int(11) DEFAULT NULL,
  `lebar` int(11) DEFAULT NULL,
  `media` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `karya_seni_2d`
--

INSERT INTO `karya_seni_2d` (`id`, `nama`, `teknik`, `pembuat`, `panjang`, `lebar`, `media`) VALUES
(2, 'Lukisan Gunung Berapi', 'Teknik Realisme', 'Budi Wicaksono', 60, 30, 'Cat Minyak'),
(3, 'Lukisan Sungai Gangga', 'Teknik Cor', 'Terania Sansa', 120, 70, 'Cat Air'),
(4, 'Lukisan Perkotaan', 'Teknik Surealisme', 'Ranika Rei', 150, 70, 'Cat Minyak'),
(5, 'Lukisan Angsa', 'Teknik Romantisme', 'Iko Rastya', 100, 60, 'Cat Minyak');

-- --------------------------------------------------------

--
-- Table structure for table `karya_seni_3d`
--

CREATE TABLE `karya_seni_3d` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `teknik` varchar(255) NOT NULL,
  `ukuran` varchar(255) DEFAULT NULL,
  `bahan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `karya_seni_3d`
--

INSERT INTO `karya_seni_3d` (`id`, `nama`, `teknik`, `ukuran`, `bahan`) VALUES
(2, 'Patung Pahlawan', 'Pahat', 'Ukuran Besar', 'Bahan Batu'),
(3, 'Patung Piramida', 'Teknik Cor', 'Kecil', 'Semen'),
(4, 'Patung Buaya', 'Teknik Pahat', 'besar', 'batu marmer'),
(5, 'Patung Seniman', 'Teknik Pahat', 'sedang', 'batu');

-- --------------------------------------------------------

--
-- Table structure for table `karya_seni_terapan`
--

CREATE TABLE `karya_seni_terapan` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `teknik` varchar(255) NOT NULL,
  `ukuran` varchar(255) DEFAULT NULL,
  `bahan` varchar(255) DEFAULT NULL,
  `fungsi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `karya_seni_terapan`
--

INSERT INTO `karya_seni_terapan` (`id`, `nama`, `teknik`, `ukuran`, `bahan`, `fungsi`) VALUES
(1, 'Kursi Rotan', 'Anyam', 'sedang', 'rotan', 'mebel'),
(2, 'Meja Ukir', 'Teknik Ukir', 'besar', 'Kayu Jati', 'mebel'),
(3, 'Vas Bunga', 'Teknik Cor', 'kecil', 'tanah liat', 'hiasan vas bunga'),
(4, 'Sapu Tangan', 'Teknik Sulam', 'kecil', 'kain', 'lap'),
(5, 'Baju Batik', 'Teknik Canting', 'sedang', 'kain dan tinta', 'pakaian');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `karya_seni_2d`
--
ALTER TABLE `karya_seni_2d`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `karya_seni_3d`
--
ALTER TABLE `karya_seni_3d`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `karya_seni_terapan`
--
ALTER TABLE `karya_seni_terapan`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `karya_seni_2d`
--
ALTER TABLE `karya_seni_2d`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `karya_seni_3d`
--
ALTER TABLE `karya_seni_3d`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `karya_seni_terapan`
--
ALTER TABLE `karya_seni_terapan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
