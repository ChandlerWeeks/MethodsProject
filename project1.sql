-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2022 at 03:19 AM
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
  `Title` char(100) DEFAULT NULL,
  `ISBN` char(20) DEFAULT NULL,
  `Author` char(20) DEFAULT NULL,
  `Genre` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`BookID`, `Title`, `ISBN`, `Author`, `Genre`) VALUES
(1, 'Wuthering Heights', '978-0593244036', 'Emily Bronte', 'Gothic Literature'),
(2, '1984', '978-0451524935', 'George Orwell', 'Dystopian Fiction'),
(4, 'To Kill a Mockingbird', '978-0446310789', 'Harper Lee', 'Southern Gothic'),
(5, ' One Hundred Years of Solitude', '978-0141184999', 'Gabriel Garcia Marqu', 'Magic realism'),
(6, 'The Fellowship of the Ring', '978-0395489314', 'J.R.R. Tolkien', 'Fantasy'),
(7, 'Beloved', '978-1784876432', 'Toni Morrison', 'Historical Fiction'),
(8, 'Dracula', '979-8721052927', 'Bram Stoker', 'Gothic Horror'),
(9, 'Watership Down', '978-0307950192', 'Richard Adams', 'Fantasy'),
(10, 'The Road Less Traveled', '978-0743238250', 'M. Scott Peck', 'Psychology'),
(11, 'The Hobbit', '978-0618260300', 'J.R.R. Tolkien', 'Fantasy');

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

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `ItemID` int(20) NOT NULL,
  `ItemName` char(100) DEFAULT NULL,
  `Price` float DEFAULT NULL,
  `Rating` float DEFAULT NULL,
  `Stock` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`ItemID`, `ItemName`, `Price`, `Rating`, `Stock`) VALUES
(1, 'Wuthering Heights', 10.99, 5, 50),
(2, 'Jaws', 12.99, 4.5, 50),
(9, '1984', 9.99, 4.9, 50),
(10, 'The Godfather', 7.99, 4.9, 50),
(11, 'The Godfather II', 7.99, 4.8, 50),
(12, 'The Shawshank Redemption', 12.99, 4.8, 50),
(13, 'The Matrix', 11.99, 4.7, 50),
(14, 'Inception', 15.99, 4.7, 50),
(15, 'The Lord of the Rings: The Fellowship of the Ring', 15.99, 4.95, 50),
(16, 'Fight Club', 13.25, 4.4, 50),
(17, 'The Dark Knight', 15.3, 4.7, 50),
(18, '12 Angry Men', 8.95, 4.8, 50),
(19, 'To Kill a Mocking Bird', 8.92, 4.7, 50),
(20, 'One Hundred Years of Solitude', 7.99, 4.2, 50),
(21, 'The Fellowship of the Ring', 7.95, 4.8, 50),
(22, 'Beloved', 6.5, 4.3, 50),
(23, 'Dracula', 9.45, 4.4, 50),
(24, 'Watership Down', 6.43, 4.2, 50),
(25, 'The Road Less Traveled', 5.99, 4.1, 50),
(26, 'The Hobbit', 9.99, 4.9, 50);

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

CREATE TABLE `movie` (
  `MovieID` int(20) NOT NULL,
  `Title` char(100) DEFAULT NULL,
  `Publisher` char(20) DEFAULT NULL,
  `Genre` char(20) DEFAULT NULL,
  `Description` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movie`
--

INSERT INTO `movie` (`MovieID`, `Title`, `Publisher`, `Genre`, `Description`) VALUES
(1, 'Jaws', 'Universal Pictures', 'Thriller', 'When a killer shark unleashes chaos on a beach community off Cape Cod, it\'s up to a local sheriff, a marine biologist, and an old seafarer to hunt the beast down.'),
(2, 'The Godfather', 'Paramount Pictures', 'Mafia', 'The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.'),
(3, 'The Shawshank Redemption', 'Columbia Pictures', 'Crime Drama', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
(4, 'The Godfather Part II', 'Paramount Pictures', 'Mafia', 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.'),
(5, 'Inception', 'Warner Bros. Picture', 'Scifi Thriller', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.'),
(6, 'The Dark Knight', 'Warner Bros. Picture', 'Superhero', 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.'),
(7, 'The Lord of the Rings: The Fellowship of the Ring', 'New Line Cinema', 'Fantasy Epic', 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.'),
(8, 'The Matrix', 'Warner Bros. Picture', 'Scifi', 'When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.'),
(9, 'Fight Club', '20th Century Fox', 'Psychological Thrill', 'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.'),
(10, '12 Angry Men', 'United Artists', 'Legal Drama', 'The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.');

-- --------------------------------------------------------

--
-- Table structure for table `orderitems`
--

CREATE TABLE `orderitems` (
  `OrderitemsID` int(20) NOT NULL,
  `OrderID` int(20) DEFAULT NULL,
  `UserID` int(20) DEFAULT NULL,
  `ItemID` int(20) DEFAULT NULL,
  `ItemName` char(20) DEFAULT NULL,
  `Price` float DEFAULT NULL,
  `Quantity` int(20) DEFAULT NULL,
  `DateTime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `OrderID` int(20) NOT NULL,
  `CartID` int(20) DEFAULT NULL,
  `UserID` int(20) DEFAULT NULL,
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
-- Indexes for table `orderitems`
--
ALTER TABLE `orderitems`
  ADD PRIMARY KEY (`OrderitemsID`),
  ADD KEY `orderitemID` (`ItemID`),
  ADD KEY `orderID` (`OrderID`),
  ADD KEY `orderitem_userID` (`UserID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `ordercartID` (`CartID`),
  ADD KEY `orderuserID` (`UserID`);

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
  MODIFY `BookID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `cartitems`
--
ALTER TABLE `cartitems`
  MODIFY `CartItemsID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `ItemID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `movie`
--
ALTER TABLE `movie`
  MODIFY `MovieID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `orderitems`
--
ALTER TABLE `orderitems`
  MODIFY `OrderitemsID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `OrderID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `shoppingcart`
--
ALTER TABLE `shoppingcart`
  MODIFY `CartID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
-- Constraints for table `orderitems`
--
ALTER TABLE `orderitems`
  ADD CONSTRAINT `orderID` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orderitemID` FOREIGN KEY (`ItemID`) REFERENCES `inventory` (`ItemID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orderitem_userID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `ordercartID` FOREIGN KEY (`CartID`) REFERENCES `shoppingcart` (`CartID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orderuserID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `shoppingcart`
--
ALTER TABLE `shoppingcart`
  ADD CONSTRAINT `cartuserID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
