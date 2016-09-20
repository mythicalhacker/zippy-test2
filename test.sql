-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Sep 20, 2016 at 11:44 AM
-- Server version: 10.1.16-MariaDB
-- PHP Version: 7.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `book_id` int(6) NOT NULL,
  `model` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `pick_time` time NOT NULL,
  `duration` time NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `mobile` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`book_id`, `model`, `date`, `pick_time`, `duration`, `timestamp`, `mobile`) VALUES
(100001, 'Pulsar 150', '2016-08-18', '06:00:00', '03:00:00', '0000-00-00 00:00:00', 9176047028);

-- --------------------------------------------------------

--
-- Table structure for table `confirmed`
--

CREATE TABLE `confirmed` (
  `vehicle_id` int(4) NOT NULL,
  `model` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `pick_time` time(6) NOT NULL,
  `drop_time` time(6) NOT NULL,
  `book_id` int(6) NOT NULL,
  `mobile` bigint(10) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `extension`
--

CREATE TABLE `extension` (
  `book_id` int(6) NOT NULL,
  `model` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `pick_time` time NOT NULL,
  `duration` time NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `mobile` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `extension`
--

INSERT INTO `extension` (`book_id`, `model`, `date`, `pick_time`, `duration`, `timestamp`, `mobile`) VALUES
(100001, 'Pulsar 150', '2016-08-18', '04:00:00', '03:00:00', '0000-00-00 00:00:00', 9176047028);

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `id` int(4) NOT NULL,
  `reg_no` varchar(4) NOT NULL,
  `model` varchar(10) NOT NULL,
  `state` int(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`id`, `reg_no`, `model`, `state`) VALUES
(1001, '0036', 'Fascino', 0),
(1002, '0250', 'Fascino', 0),
(1003, '1787', 'FZ-FI v2', 0),
(1004, '2107', 'Pulsar 150', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `extension`
--
ALTER TABLE `extension`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
