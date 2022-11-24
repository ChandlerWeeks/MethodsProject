-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 24, 2022 at 11:24 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project1`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `BookID` int(20) NOT NULL,
  `Title` char(20) DEFAULT NULL,
  `ISBN` char(20) DEFAULT NULL,
  `Author` char(20) DEFAULT NULL,
  `Genre` char(20) DEFAULT NULL,
  `Count` int(20) DEFAULT NULL,
  `Style` char(20) DEFAULT NULL,
  `Pages` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`BookID`, `Title`, `ISBN`, `Author`, `Genre`, `Count`, `Style`, `Pages`) VALUES
(1, 'Wuthering Heights', '978-0593244036', 'Emily Bronte', 'Gothic Literature', 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cartitems`
--

CREATE TABLE `cartitems` (
  `CartItemsID` int(20) NOT NULL,
  `CartID` int(20) DEFAULT NULL,
  `ItemID` int(20) DEFAULT NULL,
  `ItemName` char(20) DEFAULT NULL,
  `Price` float DEFAULT NULL,
  `Quantity` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cartitems`
--

INSERT INTO `cartitems` (`CartItemsID`, `CartID`, `ItemID`, `ItemName`, `Price`, `Quantity`) VALUES
(16, 1, 2, 'Jaws', 12.99, 1),
(17, 1, 1, 'Wuthering Heights', 10.99, 1);

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `ItemID` int(20) NOT NULL,
  `ItemName` char(20) DEFAULT NULL,
  `Price` float DEFAULT NULL,
  `Rating` float DEFAULT NULL,
  `Stock` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`ItemID`, `ItemName`, `Price`, `Rating`, `Stock`) VALUES
(1, 'Wuthering Heights', 10.99, 5, 1),
(2, 'Jaws', 12.99, 4.5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

CREATE TABLE `movie` (
  `MovieID` int(20) NOT NULL,
  `Title` char(20) DEFAULT NULL,
  `Publisher` char(20) DEFAULT NULL,
  `Genre` char(20) DEFAULT NULL,
  `Description` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movie`
--

INSERT INTO `movie` (`MovieID`, `Title`, `Publisher`, `Genre`, `Description`) VALUES
(1, 'Jaws', 'Universal Pictures', 'Thriller', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `OrderID` int(20) NOT NULL,
  `CartID` int(20) DEFAULT NULL,
  `UserID` int(20) DEFAULT NULL,
  `Price` double(20,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orderitems`
--

CREATE TABLE `orderitems` (
  `OrderitemsID` int(20) NOT NULL,
  `OrderID` int(20) DEFAULT NULL,
  `ItemID` int(20) DEFAULT NULL,
  `ItemName` char(20) DEFAULT NULL,
  `Price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `shoppingcart`
--

CREATE TABLE `shoppingcart` (
  `CartID` int(20) NOT NULL,
  `UserID` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shoppingcart`
--

INSERT INTO `shoppingcart` (`CartID`, `UserID`) VALUES
(1, 1),
(2, 10);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Email` char(20) DEFAULT NULL,
  `Password` char(20) DEFAULT NULL,
  `FirstName` char(20) DEFAULT NULL,
  `LastName` char(20) DEFAULT NULL,
  `AddressLine` char(20) DEFAULT NULL,
  `City` char(20) DEFAULT NULL,
  `State` char(20) DEFAULT NULL,
  `ZipCode` int(20) DEFAULT NULL,
  `CardNumber` int(20) DEFAULT NULL,
  `UserID` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Email`, `Password`, `FirstName`, `LastName`, `AddressLine`, `City`, `State`, `ZipCode`, `CardNumber`, `UserID`) VALUES
('test@test.com', 'test', 'Test', 'Dummy', '325 St', 'Starkville', 'MS', 39759, NULL, 1),
('fake@fake.com', 'test', 'John', 'Testman', '12 St.', 'Starkville', 'MS', 39759, 2147483647, 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`BookID`);

--
-- Indexes for table `cartitems`
--
ALTER TABLE `cartitems`
  ADD PRIMARY KEY (`CartItemsID`),
  ADD KEY `cartID` (`CartID`),
  ADD KEY `itemID` (`ItemID`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`ItemID`),
  ADD KEY `ItemName` (`ItemName`);

--
-- Indexes for table `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`MovieID`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `ordercartID` (`CartID`),
  ADD KEY `orderuserID` (`UserID`);

--
-- Indexes for table `orderitems`
--
ALTER TABLE `orderitems`
  ADD PRIMARY KEY (`OrderitemsID`),
  ADD KEY `orderID` (`OrderID`),
  ADD KEY `orderitemID` (`ItemID`);

--
-- Indexes for table `shoppingcart`
--
ALTER TABLE `shoppingcart`
  ADD PRIMARY KEY (`CartID`),
  ADD KEY `cartuserID` (`UserID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserID`),
  ADD UNIQUE KEY `UserID` (`UserID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `BookID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `cartitems`
--
ALTER TABLE `cartitems`
  MODIFY `CartItemsID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `ItemID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `movie`
--
ALTER TABLE `movie`
  MODIFY `MovieID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `orderitems`
--
ALTER TABLE `orderitems`
  MODIFY `OrderitemsID` int(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shoppingcart`
--
ALTER TABLE `shoppingcart`
  MODIFY `CartID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UserID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cartitems`
--
ALTER TABLE `cartitems`
  ADD CONSTRAINT `cartID` FOREIGN KEY (`CartID`) REFERENCES `shoppingcart` (`CartID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `itemID` FOREIGN KEY (`ItemID`) REFERENCES `inventory` (`ItemID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `ordercartID` FOREIGN KEY (`CartID`) REFERENCES `shoppingcart` (`CartID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orderuserID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `orderitems`
--
ALTER TABLE `orderitems`
  ADD CONSTRAINT `orderID` FOREIGN KEY (`OrderID`) REFERENCES `order` (`OrderID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orderitemID` FOREIGN KEY (`ItemID`) REFERENCES `inventory` (`ItemID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `shoppingcart`
--
ALTER TABLE `shoppingcart`
  ADD CONSTRAINT `cartuserID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
