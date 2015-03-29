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
	public class SimpleCsvColumnFilterTest
    {
		[Test]
		public void Test01()
		{
			// Arrange
			var originalCsvPath = Path.Combine(TestContext.CurrentContext.TestDirectory, "input.csv");
			var pathToCsvFile = Path.Combine(Path.GetDirectoryName(originalCsvPath), Path.GetFileNameWithoutExtension(originalCsvPath) + "_Test.csv");
			var delimiter = ";";
			File.Copy(originalCsvPath, pathToCsvFile, true);
			Filter sut = new Filter() { Url = pathToCsvFile, ColumnIndexToIgnore = 2, Delimiter = delimiter };

			// Act
			sut.Process();

			// Assert
			var lines = File.ReadAllLines(pathToCsvFile).Select(line => line.Split(new string[]{delimiter}, StringSplitOptions.None));

			lines.Should().OnlyContain(splittedLine => splittedLine.Length == 3);
			lines.ElementAt(0).ElementAt(0).Should().Be("A");
			lines.ElementAt(0).ElementAt(1).Should().Be("B");
			lines.ElementAt(0).ElementAt(2).Should().Be("D");
			lines.ElementAt(1).ElementAt(0).Should().Be("1");
			lines.ElementAt(1).ElementAt(1).Should().Be("2");
			lines.ElementAt(1).ElementAt(2).Should().Be("4");

		}
    }
}
