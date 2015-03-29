using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Linq;

namespace SimpleCsvColumnFilter
{
	public class Filter
	{
		public string Url { get; set; }

		public int ColumnIndexToIgnore { get; set; }
		
		public void Process()
		{
			var splitLines = File.ReadAllLines(Url).Select(line => line.Split(new []{Delimiter}, StringSplitOptions.None));

			var filteredLines = splitLines.Select(splitLine => splitLine.Take(ColumnIndexToIgnore).Concat(splitLine.Skip(ColumnIndexToIgnore+1))).Select(line => string.Join(Delimiter, line.ToArray()));

			File.Delete(Url);
			File.WriteAllLines(Url, filteredLines);
		}

		public string Delimiter { get; set; }
	}
}
