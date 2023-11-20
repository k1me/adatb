-- --------------------------------------------------------
-- Hoszt:                        127.0.0.1
-- Szerver verzió:               11.1.2-MariaDB - mariadb.org binary distribution
-- Szerver OS:                   Win64
-- HeidiSQL Verzió:              12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Adatbázis struktúra mentése a szalloda.
CREATE DATABASE IF NOT EXISTS `szalloda` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `szalloda`;

-- Struktúra mentése tábla szalloda. felhasznalo
CREATE TABLE IF NOT EXISTS `felhasznalo` (
  `felhasznalonev` varchar(255) NOT NULL,
  `nev` varchar(255) NOT NULL,
  `jelszo` varchar(255) NOT NULL,
  PRIMARY KEY (`felhasznalonev`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.felhasznalo: ~4 rows (hozzávetőleg)
INSERT INTO `felhasznalo` (`felhasznalonev`, `nev`, `jelszo`) VALUES
	('kiskati03', 'Kiss Katalin', '$5$rounds=535000$pFTkfaGryqghvI2W$iYUTjhssNzOZfXdX2vacGZJ1ueM5S/7Qcm7u3xQqVxB'),
	('kovacspali45', 'Kovács Pál', '$5$rounds=535000$BjXNrIgB1IzNwow8$0VtnEyLTm9D7944i1M/rTpx/SrnKbk488c55ra7XIh6'),
	('nagyanti', 'Nagy Antal', '$5$rounds=535000$C9pqnTg6sGrz861A$awqTBV4ujtDg7faNHJMtI0zrVg9rhQ1TUW2KvNibNQ6'),
	('recisrobi01', 'Recepciós Róbert', '$5$rounds=535000$Iw9XLVVJ.t3hXsEM$suKGiseMUahS37Qvr0ddjiYdI7.So7yyAmusXMziGW2');

-- Struktúra mentése tábla szalloda. foglalas
CREATE TABLE IF NOT EXISTS `foglalas` (
  `email` varchar(255) NOT NULL,
  `mettol` date NOT NULL,
  `meddig` date NOT NULL,
  `fizetendo` int(11) NOT NULL DEFAULT 0,
  KEY `mettol` (`mettol`),
  KEY `meddig` (`meddig`),
  KEY `foglalas.vendeg` (`email`),
  CONSTRAINT `foglalas.vendeg` FOREIGN KEY (`email`) REFERENCES `vendeg` (`email`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.foglalas: ~1 rows (hozzávetőleg)
INSERT INTO `foglalas` (`email`, `mettol`, `meddig`, `fizetendo`) VALUES
	('ferdinandv@habslot.at', '2023-11-20', '2023-11-26', 324000);

-- Struktúra mentése tábla szalloda. kezeli
CREATE TABLE IF NOT EXISTS `kezeli` (
  `felhasznalonev` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `mettol` date NOT NULL,
  `meddig` date NOT NULL,
  KEY `kezeli.email` (`email`),
  KEY `kezeli.felhasznalonev` (`felhasznalonev`),
  KEY `kezeli.meddig` (`meddig`),
  KEY `kezeli.mettol` (`mettol`),
  CONSTRAINT `kezeli.email` FOREIGN KEY (`email`) REFERENCES `vendeg` (`email`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `kezeli.felhasznalonev` FOREIGN KEY (`felhasznalonev`) REFERENCES `felhasznalo` (`felhasznalonev`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `kezeli.meddig` FOREIGN KEY (`meddig`) REFERENCES `foglalas` (`meddig`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `kezeli.mettol` FOREIGN KEY (`mettol`) REFERENCES `foglalas` (`mettol`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.kezeli: ~1 rows (hozzávetőleg)
INSERT INTO `kezeli` (`felhasznalonev`, `email`, `mettol`, `meddig`) VALUES
	('kiskati03', 'ferdinandv@habslot.at', '2023-11-20', '2023-11-26');

-- Struktúra mentése tábla szalloda. szoba
CREATE TABLE IF NOT EXISTS `szoba` (
  `szobaszam` int(11) NOT NULL,
  `megnevezes` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`szobaszam`),
  KEY `szoba.megnevezes` (`megnevezes`),
  CONSTRAINT `szoba.megnevezes` FOREIGN KEY (`megnevezes`) REFERENCES `szobatipus` (`megnevezes`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.szoba: ~25 rows (hozzávetőleg)
INSERT INTO `szoba` (`szobaszam`, `megnevezes`) VALUES
	(3, 'Családi lakosztály'),
	(13, 'Családi lakosztály'),
	(22, 'Családi lakosztály'),
	(43, 'Családi lakosztály'),
	(5, 'Deluxe lakosztály'),
	(15, 'Deluxe lakosztály'),
	(24, 'Deluxe lakosztály'),
	(42, 'Deluxe lakosztály'),
	(2, 'Klasszikus egyágyas'),
	(11, 'Klasszikus egyágyas'),
	(31, 'Klasszikus egyágyas'),
	(33, 'Klasszikus egyágyas'),
	(23, 'Panoráma apartman'),
	(32, 'Panoráma apartman'),
	(35, 'Panoráma apartman'),
	(41, 'Panoráma apartman'),
	(44, 'Panoráma apartman'),
	(1, 'Superior kétágyas'),
	(4, 'Superior kétágyas'),
	(12, 'Superior kétágyas'),
	(14, 'Superior kétágyas'),
	(21, 'Superior kétágyas'),
	(25, 'Superior kétágyas'),
	(34, 'Superior kétágyas'),
	(45, 'Superior kétágyas');

-- Struktúra mentése tábla szalloda. szobaja
CREATE TABLE IF NOT EXISTS `szobaja` (
  `szobaszam` int(255) NOT NULL DEFAULT 0,
  `mettol` date NOT NULL,
  `meddig` date NOT NULL,
  `email` varchar(255) NOT NULL,
  KEY `szobaja.szobaszam` (`szobaszam`),
  KEY `szobaja.email` (`email`),
  KEY `szobaja.meddig` (`meddig`),
  KEY `szobaja.mettol` (`mettol`),
  CONSTRAINT `szobaja.email` FOREIGN KEY (`email`) REFERENCES `foglalas` (`email`) ON DELETE CASCADE,
  CONSTRAINT `szobaja.meddig` FOREIGN KEY (`meddig`) REFERENCES `foglalas` (`meddig`) ON DELETE CASCADE,
  CONSTRAINT `szobaja.mettol` FOREIGN KEY (`mettol`) REFERENCES `foglalas` (`mettol`) ON DELETE CASCADE,
  CONSTRAINT `szobaja.szobaszam` FOREIGN KEY (`szobaszam`) REFERENCES `szoba` (`szobaszam`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.szobaja: ~2 rows (hozzávetőleg)
INSERT INTO `szobaja` (`szobaszam`, `mettol`, `meddig`, `email`) VALUES
	(3, '2023-11-20', '2023-11-26', 'ferdinandv@habslot.at'),
	(5, '2023-11-20', '2023-11-26', 'ferdinandv@habslot.at');

-- Struktúra mentése tábla szalloda. szobatipus
CREATE TABLE IF NOT EXISTS `szobatipus` (
  `megnevezes` varchar(255) NOT NULL,
  `napi_ar` int(11) NOT NULL,
  `fekvohelyek_szama` int(11) NOT NULL,
  `leiras` text NOT NULL,
  PRIMARY KEY (`megnevezes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.szobatipus: ~6 rows (hozzávetőleg)
INSERT INTO `szobatipus` (`megnevezes`, `napi_ar`, `fekvohelyek_szama`, `leiras`) VALUES
	('Családi lakosztály', 29990, 5, 'Kényelmes és tágas lakosztály nagy családoknak'),
	('Deluxe lakosztály', 23890, 4, 'Elegáns lakosztály külön nappalival és hálószobával.'),
	('Klasszikus egyágyas', 13990, 1, 'Kényelmes szoba egyágyas ággyal.'),
	('Panoráma apartman', 24990, 3, 'Gyönyörű panorámás kilátással rendelkező apartman.'),
	('Superior kétágyas', 17990, 2, 'Modern és tágas szoba két külön ággyal.');

-- Struktúra mentése tábla szalloda. vendeg
CREATE TABLE IF NOT EXISTS `vendeg` (
  `email` varchar(255) NOT NULL,
  `nev` varchar(255) NOT NULL,
  `telefonszam` varchar(20) NOT NULL,
  `szuletesi_datum` date NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.vendeg: ~7 rows (hozzávetőleg)
INSERT INTO `vendeg` (`email`, `nev`, `telefonszam`, `szuletesi_datum`) VALUES
	('ferdinandv@habslot.at', 'Ferdinánd Károly Lipót József Ferenc Marcellin', '06707779875', '1793-03-19'),
	('ferencjozsef@habslot.at', 'I. Ferenc József', '06707779876', '1830-08-18'),
	('kiakaroly@habslot.at', 'Karl Franz Josef Ludwig Hubert Georg Maria von Österreich', '06707779877', '1887-08-17'),
	('luxzsiga@luxemburg.lu', 'Luxemburgi Zsigmond', '06304567891', '1368-03-31'),
	('mariaterezia@habsburg.at', 'Mária Terézia', '06707779874', '1717-05-13'),
	('matyasazigazsagos@hunyadi.hu', 'Hunyadi Mátyás', '06207771234', '1443-02-23'),
	('ulaszlo02@jagello.lt', 'Dobzse László', '06707779873', '1456-03-01');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
