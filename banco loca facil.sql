-- MySQL Script generated by MySQL Workbench
-- Fri Oct 25 15:05:02 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `locafacil` DEFAULT CHARACTER SET utf8 ;
USE `locafacil` ;

-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `telephone` VARCHAR(11) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `sex` VARCHAR(9) NOT NULL,
  `user` VARCHAR(20) NOT NULL,
  `password` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`iduser`, `cpf`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC),
  UNIQUE INDEX `user_UNIQUE` (`user` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`rent`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rent` (
  `idrent` INT NOT NULL,
  `description` VARCHAR(200) NULL,
  `neighborhood` VARCHAR(45) NOT NULL,
  `situation` TINYINT NOT NULL,
  `street` VARCHAR(45) NOT NULL,
  `number` INT NOT NULL,
  `complement` VARCHAR(45) NULL,
  `cep` VARCHAR(8) NOT NULL,
  `price` FLOAT NOT NULL,
  `id_user` INT NOT NULL,
  PRIMARY KEY (`idrent`, `id_user`),
  INDEX `id_user_idx` (`id_user` ASC),
  CONSTRAINT `id_user`
    FOREIGN KEY (`id_user`)
    REFERENCES `locafacil`.`user` (`iduser`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`images`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `images` (
  `source` VARCHAR(200) NOT NULL,
  `id_rent` INT NOT NULL,
  PRIMARY KEY (`id_rent`),
  CONSTRAINT `id_rent`
    FOREIGN KEY (`id_rent`)
    REFERENCES `locafacil`.`rent` (`idrent`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
