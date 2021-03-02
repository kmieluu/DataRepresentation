SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


--
-- Table structure for table `dogs`
--

DROP TABLE IF EXISTS `dogs`;
CREATE TABLE `dogs` (
  IKCReg varchar(100) NOT NULL,
  RegNum int(20) NOT NULL,
  age int (10) NOT NULL,
  breed varchar(100) NOT NULL,
  price int(10) NOT NULL,
  id int(10) NOT NULL, 
  PRIMARY KEY (id)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `dogs`
--

INSERT INTO `dogs` (IKCReg, RegNum, age, breed, price, id) VALUES
('Yes', 12000, 2, "pudle", 100, 1),
('Yes', 12000, 1, "chiuaua", 123, 2),
('Yes', 1234, 4, "husky", 2000, 3),
('Yes', 12000, 1, "german shepherd", 1000, 4),
('Yes', 96336, 3, "doodle", 2123, 5),
('Yes', 12000, 4, "berneese", 30, 6),
('Yes', 654654, 1, "vizsla", 300, 7),
('Yes', 987987, 2, "mix race",120, 8);

-- --------------------------------------------------------

--
-- Table structure for table `competitions`
--

DROP TABLE IF EXISTS `competitions`;
CREATE TABLE competitions (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  'descr' varchar(250) NOT NULL,
  'participants' int(5) NOT NULL,
  'prize' varchar(250) NOT NULL,
  PRIMARY KEY ('id')
  UNIQUE KEY `descr` (`descr`)
  )
  ;
 
--
-- Dumping data for table `competitions`
--

INSERT INTO `competitions` (`id`, `descr`, `participants`, `prize`) VALUES
(1, "Championship of Sydney", 200, "$ 1000"),
(3, "Championship of Moscow", 40, "$ 10000"),
(5, "Championship of Dublin", 60, "$ 10000");

-- --------------------------------------------------------

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
CREATE TABLE IF NOT EXISTS `countries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owners name` varchar(30) NOT NULL,
  `Level of knowledge` varchar(50) NOT NULL,
  
  PRIMARY KEY (`id`),
  UNIQUE KEY `owners name` (`owners name`)
) 
--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`id`, `owners name`, `Level of knowledge`) VALUES
(11, 'Alex Baldwin', 'Pro owner'),
(12, 'Stanislaw Sojka', 'Beginner'),
(13, 'Sarah Jessica Parker', 'Pro owner');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;