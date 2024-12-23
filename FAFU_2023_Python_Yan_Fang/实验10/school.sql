USE [master]
GO
/****** Object:  Database [School]    Script Date: 2024/5/7 23:29:55 ******/
CREATE DATABASE [School]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'School', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA\School.mdf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'School_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL11.MSSQLSERVER\MSSQL\DATA\School_log.ldf' , SIZE = 2048KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO
ALTER DATABASE [School] SET COMPATIBILITY_LEVEL = 110
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [School].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [School] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [School] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [School] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [School] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [School] SET ARITHABORT OFF 
GO
ALTER DATABASE [School] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [School] SET AUTO_CREATE_STATISTICS ON 
GO
ALTER DATABASE [School] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [School] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [School] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [School] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [School] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [School] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [School] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [School] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [School] SET  DISABLE_BROKER 
GO
ALTER DATABASE [School] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [School] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [School] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [School] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [School] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [School] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [School] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [School] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [School] SET  MULTI_USER 
GO
ALTER DATABASE [School] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [School] SET DB_CHAINING OFF 
GO
ALTER DATABASE [School] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [School] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
USE [School]
GO
/****** Object:  Table [dbo].[SC]    Script Date: 2024/5/7 23:29:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[SC](
	[Sno] [varchar](255) NOT NULL,
	[Cno] [varchar](255) NOT NULL,
	[Grade] [int] NOT NULL,
 CONSTRAINT [PK_SC] PRIMARY KEY CLUSTERED 
(
	[Sno] ASC,
	[Cno] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[student]    Script Date: 2024/5/7 23:29:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[student](
	[Sno] [varchar](12) NOT NULL,
	[Sname] [varchar](12) NOT NULL,
	[Ssex] [varchar](2) NULL,
	[Sage] [int] NULL,
 CONSTRAINT [PK_student] PRIMARY KEY CLUSTERED 
(
	[Sno] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10001', N'00002', 90)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10001', N'00005', 91)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10002', N'00002', 79)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10002', N'00003', 86)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10002', N'00004', 70)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10003', N'00001', 85)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10003', N'00002', 83)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10004', N'00002', 77)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10004', N'00003', 67)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10005', N'00001', 88)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10005', N'00003', 98)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10005', N'00004', 50)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10006', N'00006', 70)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10006', N'00007', 88)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10007', N'00006', 30)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10007', N'00008', 58)
INSERT [dbo].[SC] ([Sno], [Cno], [Grade]) VALUES (N'10008', N'00001', 60)
INSERT [dbo].[student] ([Sno], [Sname], [Ssex], [Sage]) VALUES (N'10001', N'Jack', N'M', 18)
INSERT [dbo].[student] ([Sno], [Sname], [Ssex], [Sage]) VALUES (N'10002', N'Jackie', N'F', 18)
INSERT [dbo].[student] ([Sno], [Sname], [Ssex], [Sage]) VALUES (N'10003', N'Cindy', N'M', 19)
INSERT [dbo].[student] ([Sno], [Sname], [Ssex], [Sage]) VALUES (N'10004', N'Chason', N'F', 20)
INSERT [dbo].[student] ([Sno], [Sname], [Ssex], [Sage]) VALUES (N'10005', N'Lisa', N'F', 19)
INSERT [dbo].[student] ([Sno], [Sname], [Ssex], [Sage]) VALUES (N'10006', N'Michael', N'M', 19)
INSERT [dbo].[student] ([Sno], [Sname], [Ssex], [Sage]) VALUES (N'10007', N'Mia', N'F', 19)
INSERT [dbo].[student] ([Sno], [Sname], [Ssex], [Sage]) VALUES (N'10008', N'Hower', N'M', 18)
INSERT [dbo].[student] ([Sno], [Sname], [Ssex], [Sage]) VALUES (N'10009', N'Hepburn', N'M', 20)
USE [master]
GO
ALTER DATABASE [School] SET  READ_WRITE 
GO
