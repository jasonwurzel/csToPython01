using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using FluentAssertions;

namespace SimpleCsvColumnFilter
{
	[TestFixture]
	public class SimpleCsvColumnFilterTests
    {
		[Test]
		public void Test01()
		{
			// Arrange
			var originalCsvPath = Path.Combine(TestContext.CurrentContext.TestDirectory, @"..\..\..\Tests\FilterThirdCol\input.csv");
			var expectedCsvPath = Path.Combine(TestContext.CurrentContext.TestDirectory, @"..\..\..\Tests\FilterThirdCol\expected.csv");
			var pathToCsvFile = Path.Combine(Path.GetDirectoryName(originalCsvPath), Path.GetFileNameWithoutExtension(originalCsvPath) + "_Test_cs.csv");
			var delimiter = ";";
			File.Copy(originalCsvPath, pathToCsvFile, true);
			Filter sut = new Filter() { Url = pathToCsvFile, ColumnIndexToIgnore = 2, Delimiter = delimiter };

			// Act
			sut.Process();

			// Assert
			var lines = File.ReadAllLines(pathToCsvFile);
			var expectedLines = File.ReadAllLines(expectedCsvPath);
			lines.Should().Equal(expectedLines);

			
			
			File.Delete(pathToCsvFile);
		}
    }
}
