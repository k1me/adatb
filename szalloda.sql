-- --------------------------------------------------------
-- Hoszt:                        127.0.0.1
-- Szerver verzió:               11.1.2-MariaDB - mariadb.org binary distribution
-- Szerver OS:                   Win64
-- HeidiSQL Verzió:              12.3.0.6589
-- --------------------------------------------------------
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */
;

/*!40101 SET NAMES utf8 */
;

/*!50503 SET NAMES utf8mb4 */
;

/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */
;

/*!40103 SET TIME_ZONE='+00:00' */
;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */
;

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */
;

/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */
;

-- Adatbázis struktúra mentése a szalloda.
CREATE DATABASE IF NOT EXISTS `szalloda`
/*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */
;

USE `szalloda`;

-- Struktúra mentése tábla szalloda. felhasznalo
CREATE TABLE IF NOT EXISTS `felhasznalo` (
	`felhasznalonev` varchar(255) NOT NULL,
	`nev` varchar(255) NOT NULL,
	`jelszo` varchar(255) NOT NULL,
	PRIMARY KEY (`felhasznalonev`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.felhasznalo: ~4 rows (hozzávetőleg)
INSERT INTO
	`felhasznalo` (`felhasznalonev`, `nev`, `jelszo`)
VALUES
	(
		'kiskati03',
		'Kiss Katalin',
		'$5$rounds=535000$pFTkfaGryqghvI2W$iYUTjhssNzOZfXdX2vacGZJ1ueM5S/7Qcm7u3xQqVxB'
	),
	(
		'kovacspali45',
		'Kovács Pál',
		'$5$rounds=535000$BjXNrIgB1IzNwow8$0VtnEyLTm9D7944i1M/rTpx/SrnKbk488c55ra7XIh6'
	),
	(
		'nagyanti',
		'Nagy Antal',
		'$5$rounds=535000$C9pqnTg6sGrz861A$awqTBV4ujtDg7faNHJMtI0zrVg9rhQ1TUW2KvNibNQ6'
	),
	(
		'recisrobi01',
		'Recepciós Róbert',
		'$5$rounds=535000$Iw9XLVVJ.t3hXsEM$suKGiseMUahS37Qvr0ddjiYdI7.So7yyAmusXMziGW2'
	);

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
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.foglalas: ~14 rows (hozzávetőleg)
INSERT INTO
	`foglalas` (`email`, `mettol`, `meddig`, `fizetendo`)
VALUES
	(
		'ferencjozsef@habslot.at',
		'2023-12-12',
		'2023-12-15',
		89970
	),
	(
		'kiakaroly@habslot.at',
		'2023-11-21',
		'2023-11-24',
		167940
	),
	(
		'mariaterezia@habsburg.at',
		'2023-11-30',
		'2023-12-03',
		95940
	),
	(
		'ferdinandv@habslot.at',
		'2023-11-27',
		'2023-12-03',
		527760
	),
	(
		'matyasazigazsagos@hunyadi.hu',
		'2023-12-03',
		'2023-12-10',
		272860
	),
	(
		'luxzsiga@luxemburg.lu',
		'2023-12-03',
		'2023-12-07',
		319880
	),
	(
		'ulaszlo02@jagello.lt',
		'2023-12-14',
		'2023-12-19',
		344850
	),
	(
		'kiakaroly@habslot.at',
		'2023-12-10',
		'2023-12-21',
		758670
	),
	(
		'ferencjozsef@habslot.at',
		'2023-12-27',
		'2024-01-02',
		299880
	),
	(
		'mariaterezia@habsburg.at',
		'2023-12-06',
		'2023-12-12',
		257880
	),
	(
		'ferdinandv@habslot.at',
		'2024-01-01',
		'2024-01-08',
		356860
	),
	(
		'matyasazigazsagos@hunyadi.hu',
		'2023-12-29',
		'2024-01-06',
		695680
	),
	(
		'luxzsiga@luxemburg.lu',
		'2024-01-11',
		'2024-01-12',
		13990
	),
	(
		'ferencjozsef@habslot.at',
		'2024-01-21',
		'2024-02-01',
		285890
	);

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
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.kezeli: ~14 rows (hozzávetőleg)
INSERT INTO
	`kezeli` (`felhasznalonev`, `email`, `mettol`, `meddig`)
VALUES
	(
		'recisrobi01',
		'ferencjozsef@habslot.at',
		'2023-12-12',
		'2023-12-15'
	),
	(
		'nagyanti',
		'kiakaroly@habslot.at',
		'2023-11-21',
		'2023-11-24'
	),
	(
		'kiskati03',
		'mariaterezia@habsburg.at',
		'2023-11-30',
		'2023-12-03'
	),
	(
		'nagyanti',
		'ferdinandv@habslot.at',
		'2023-11-27',
		'2023-12-03'
	),
	(
		'kovacspali45',
		'matyasazigazsagos@hunyadi.hu',
		'2023-12-03',
		'2023-12-10'
	),
	(
		'kovacspali45',
		'luxzsiga@luxemburg.lu',
		'2023-12-03',
		'2023-12-07'
	),
	(
		'kiskati03',
		'ulaszlo02@jagello.lt',
		'2023-12-14',
		'2023-12-19'
	),
	(
		'recisrobi01',
		'kiakaroly@habslot.at',
		'2023-12-10',
		'2023-12-21'
	),
	(
		'nagyanti',
		'ferencjozsef@habslot.at',
		'2023-12-27',
		'2024-01-02'
	),
	(
		'kiskati03',
		'mariaterezia@habsburg.at',
		'2023-12-06',
		'2023-12-12'
	),
	(
		'kiskati03',
		'ferdinandv@habslot.at',
		'2024-01-01',
		'2024-01-08'
	),
	(
		'kiskati03',
		'matyasazigazsagos@hunyadi.hu',
		'2023-12-29',
		'2024-01-06'
	),
	(
		'kiskati03',
		'luxzsiga@luxemburg.lu',
		'2024-01-11',
		'2024-01-12'
	),
	(
		'kiskati03',
		'ferencjozsef@habslot.at',
		'2024-01-21',
		'2024-02-01'
	);

-- Struktúra mentése tábla szalloda. szoba
CREATE TABLE IF NOT EXISTS `szoba` (
	`szobaszam` int(11) NOT NULL,
	`megnevezes` varchar(255) NOT NULL DEFAULT '',
	PRIMARY KEY (`szobaszam`),
	KEY `szoba.megnevezes` (`megnevezes`),
	CONSTRAINT `szoba.megnevezes` FOREIGN KEY (`megnevezes`) REFERENCES `szobatipus` (`megnevezes`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.szoba: ~25 rows (hozzávetőleg)
INSERT INTO
	`szoba` (`szobaszam`, `megnevezes`)
VALUES
	(3, 'Családi lakosztály'),
	(13, 'Családi lakosztály'),
	(23, 'Családi lakosztály'),
	(33, 'Családi lakosztály'),
	(43, 'Családi lakosztály'),
	(4, 'Deluxe lakosztály'),
	(14, 'Deluxe lakosztály'),
	(24, 'Deluxe lakosztály'),
	(34, 'Deluxe lakosztály'),
	(44, 'Deluxe lakosztály'),
	(1, 'Klasszikus egyágyas'),
	(11, 'Klasszikus egyágyas'),
	(21, 'Klasszikus egyágyas'),
	(31, 'Klasszikus egyágyas'),
	(41, 'Klasszikus egyágyas'),
	(5, 'Panoráma apartman'),
	(25, 'Panoráma apartman'),
	(35, 'Panoráma apartman'),
	(45, 'Panoráma apartman'),
	(2, 'Superior kétágyas'),
	(12, 'Superior kétágyas'),
	(15, 'Superior kétágyas'),
	(22, 'Superior kétágyas'),
	(32, 'Superior kétágyas'),
	(42, 'Superior kétágyas');

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
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.szobaja: ~31 rows (hozzávetőleg)
INSERT INTO
	`szobaja` (`szobaszam`, `mettol`, `meddig`, `email`)
VALUES
	(
		3,
		'2023-12-12',
		'2023-12-15',
		'ferencjozsef@habslot.at'
	),
	(
		13,
		'2023-11-21',
		'2023-11-24',
		'kiakaroly@habslot.at'
	),
	(
		15,
		'2023-11-21',
		'2023-11-24',
		'kiakaroly@habslot.at'
	),
	(
		2,
		'2023-11-30',
		'2023-12-03',
		'mariaterezia@habsburg.at'
	),
	(
		1,
		'2023-11-30',
		'2023-12-03',
		'mariaterezia@habsburg.at'
	),
	(
		3,
		'2023-11-27',
		'2023-12-03',
		'ferdinandv@habslot.at'
	),
	(
		4,
		'2023-11-27',
		'2023-12-03',
		'ferdinandv@habslot.at'
	),
	(
		31,
		'2023-11-27',
		'2023-12-03',
		'ferdinandv@habslot.at'
	),
	(
		5,
		'2023-11-27',
		'2023-12-03',
		'ferdinandv@habslot.at'
	),
	(
		11,
		'2023-12-03',
		'2023-12-10',
		'matyasazigazsagos@hunyadi.hu'
	),
	(
		23,
		'2023-12-03',
		'2023-12-10',
		'matyasazigazsagos@hunyadi.hu'
	),
	(
		13,
		'2023-12-03',
		'2023-12-07',
		'luxzsiga@luxemburg.lu'
	),
	(
		25,
		'2023-12-03',
		'2023-12-07',
		'luxzsiga@luxemburg.lu'
	),
	(
		25,
		'2023-12-03',
		'2023-12-07',
		'luxzsiga@luxemburg.lu'
	),
	(
		5,
		'2023-12-14',
		'2023-12-19',
		'ulaszlo02@jagello.lt'
	),
	(
		2,
		'2023-12-14',
		'2023-12-19',
		'ulaszlo02@jagello.lt'
	),
	(
		34,
		'2023-12-14',
		'2023-12-19',
		'ulaszlo02@jagello.lt'
	),
	(
		35,
		'2023-12-10',
		'2023-12-21',
		'kiakaroly@habslot.at'
	),
	(
		42,
		'2023-12-10',
		'2023-12-21',
		'kiakaroly@habslot.at'
	),
	(
		24,
		'2023-12-10',
		'2023-12-21',
		'kiakaroly@habslot.at'
	),
	(
		5,
		'2023-12-27',
		'2024-01-02',
		'ferencjozsef@habslot.at'
	),
	(
		5,
		'2023-12-27',
		'2024-01-02',
		'ferencjozsef@habslot.at'
	),
	(
		5,
		'2023-12-06',
		'2023-12-12',
		'mariaterezia@habsburg.at'
	),
	(
		22,
		'2023-12-06',
		'2023-12-12',
		'mariaterezia@habsburg.at'
	),
	(
		25,
		'2024-01-01',
		'2024-01-08',
		'ferdinandv@habslot.at'
	),
	(
		4,
		'2024-01-01',
		'2024-01-08',
		'ferdinandv@habslot.at'
	),
	(
		35,
		'2023-12-29',
		'2024-01-06',
		'matyasazigazsagos@hunyadi.hu'
	),
	(
		1,
		'2023-12-29',
		'2024-01-06',
		'matyasazigazsagos@hunyadi.hu'
	),
	(
		43,
		'2023-12-29',
		'2024-01-06',
		'matyasazigazsagos@hunyadi.hu'
	),
	(
		22,
		'2023-12-29',
		'2024-01-06',
		'matyasazigazsagos@hunyadi.hu'
	),
	(
		1,
		'2024-01-11',
		'2024-01-12',
		'luxzsiga@luxemburg.lu'
	),
	(
		44,
		'2024-01-21',
		'2024-02-01',
		'ferencjozsef@habslot.at'
	);

-- Struktúra mentése tábla szalloda. szobatipus
CREATE TABLE IF NOT EXISTS `szobatipus` (
	`megnevezes` varchar(255) NOT NULL,
	`napi_ar` int(11) NOT NULL,
	`fekvohelyek_szama` int(11) NOT NULL,
	`leiras` text NOT NULL,
	PRIMARY KEY (`megnevezes`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.szobatipus: ~6 rows (hozzávetőleg)
INSERT INTO
	`szobatipus` (
		`megnevezes`,
		`napi_ar`,
		`fekvohelyek_szama`,
		`leiras`
	)
VALUES
	(
		'Családi lakosztály',
		29990,
		5,
		'Kényelmes és tágas lakosztály nagy családoknak'
	),
	(
		'Deluxe lakosztály',
		25990,
		4,
		'Elegáns lakosztály külön nappalival és hálószobával.'
	),
	(
		'Klasszikus egyágyas',
		13990,
		1,
		'Kényelmes szoba egyágyas ággyal.'
	),
	(
		'Panoráma apartman',
		24990,
		3,
		'Gyönyörű panorámás kilátással rendelkező apartman.'
	),
	(
		'Superior kétágyas',
		17990,
		2,
		'Modern és tágas szoba két külön ággyal.'
	);

-- Struktúra mentése tábla szalloda. vendeg
CREATE TABLE IF NOT EXISTS `vendeg` (
	`email` varchar(255) NOT NULL,
	`nev` varchar(255) NOT NULL,
	`telefonszam` varchar(20) NOT NULL,
	`szuletesi_datum` date NOT NULL,
	PRIMARY KEY (`email`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- Tábla adatainak mentése szalloda.vendeg: ~7 rows (hozzávetőleg)
INSERT INTO
	`vendeg` (`email`, `nev`, `telefonszam`, `szuletesi_datum`)
VALUES
	(
		'ferdinandv@habslot.at',
		'Ferdinánd Károly Lipót József Ferenc Marcellin',
		'06707779875',
		'1793-03-19'
	),
	(
		'ferencjozsef@habslot.at',
		'I. Ferenc József',
		'06707779876',
		'1830-08-18'
	),
	(
		'kiakaroly@habslot.at',
		'Karl Franz Josef Ludwig Hubert Georg Maria von Österreich',
		'06707779877',
		'1887-08-17'
	),
	(
		'luxzsiga@luxemburg.lu',
		'Luxemburgi Zsigmond',
		'06304567891',
		'1368-03-31'
	),
	(
		'mariaterezia@habsburg.at',
		'Mária Terézia',
		'06707779874',
		'1717-05-13'
	),
	(
		'matyasazigazsagos@hunyadi.hu',
		'Hunyadi Mátyás',
		'06207771234',
		'1443-02-23'
	),
	(
		'ulaszlo02@jagello.lt',
		'Dobzse László',
		'06707779873',
		'1456-03-01'
	);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */
;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */
;

/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */
;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */
;

/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */
;