-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 16, 2020 lúc 11:37 AM
-- Phiên bản máy phục vụ: 10.4.8-MariaDB
-- Phiên bản PHP: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlsx_dves`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `save_data`
--

CREATE TABLE `save_data` (
  `STT` int(11) NOT NULL,
  `Auto` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Time Push` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ID` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `S1` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `S2` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `On/Off` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `RFID` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Barcode` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Amp` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Freg` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `MaxFreg` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT current_timestamp(),
  `Counter` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL,
  `TimeFree` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `KWH` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `RealTime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `save_data`
--
ALTER TABLE `save_data`
  ADD PRIMARY KEY (`STT`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `save_data`
--
ALTER TABLE `save_data`
  MODIFY `STT` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
