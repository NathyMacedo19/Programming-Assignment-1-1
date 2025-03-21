#
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `ID` int(11) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `balance` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `accounts` (`ID`, `firstname`, `lastname`, `address`, `balance`) VALUES
(103, 'Bobby', 'Ewing', 'South Fork', 2058),
(108, 'Yanni', 'Zao', 'Bejing', 50000),
(112, 'Patricia', 'Smith', 'Belfast', 52500),
(135, 'Darren', 'Gillespie', 'London', 3050),
(141, 'Eric', 'Bond', 'Kensington', 1000);

-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`ID`);
  
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=160;